/* Общий скрипт сайта. Подключается на всех страницах. */
(function () {
  'use strict';

  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = matchMedia('(hover: hover) and (pointer: fine)').matches;
  var doc = document.documentElement;
  var $ = function (id) { return document.getElementById(id); };

  var yr = $('yr'); if (yr) yr.textContent = new Date().getFullYear();

  /* Тема оформления */
  var THEME_KEY = 'tr-theme';
  var themeBtn = $('theme');
  var themeMeta = document.querySelector('meta[name="theme-color"]');
  var setTheme = function (name) {
    doc.setAttribute('data-theme', name);
    if (themeMeta) themeMeta.setAttribute('content', name === 'dark' ? '#0e1216' : '#ffffff');
    if (themeBtn) {
      themeBtn.setAttribute('aria-pressed', name === 'dark' ? 'true' : 'false');
      themeBtn.setAttribute('aria-label', name === 'dark' ? 'Включить светлую тему' : 'Включить тёмную тему');
    }
  };
  setTheme(doc.getAttribute('data-theme') === 'dark' ? 'dark' : 'light');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var next = doc.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      setTheme(next);
      try { localStorage.setItem(THEME_KEY, next); } catch (e) {}
    });
  }

  /* Экран загрузки */
  var load = $('load');
  if (load) {
    var lLine = $('loadLine'), lPct = $('loadPct'),
        shown = 0, aim = 0, finished = false, raf = null;

    var paint = function () {
      if (shown < aim) shown += Math.max(.6, (aim - shown) / 9);
      if (shown > aim) shown = aim;
      lPct.textContent = ('0' + Math.floor(shown)).slice(-2);
      lLine.style.transform = 'scaleX(' + (shown / 100) + ')';
      if (shown < 100) raf = requestAnimationFrame(paint);
    };
    var finish = function () {
      if (finished) return;
      finished = true;
      aim = 100;
      setTimeout(function () {
        cancelAnimationFrame(raf);
        shown = 100; lPct.textContent = '100'; lLine.style.transform = 'scaleX(1)';
        setTimeout(function () {
          load.classList.add('out');
          doc.classList.add('load-done');
          setTimeout(function () { load.hidden = true; }, 1250);
        }, 380);
      }, 420);
    };

    if (reduce) {
      load.hidden = true;
      doc.classList.add('load-done');
    } else {
      load.classList.add('go');
      raf = requestAnimationFrame(paint);
      var steps = 0;
      var step = function () { steps++; aim = Math.max(aim, 24 + steps * 38); if (steps >= 2) finish(); };
      var first = document.querySelector('[data-hero-img]');
      if (!first || first.complete) step();
      else { first.addEventListener('load', step); first.addEventListener('error', step); }
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(step); else step();
      setTimeout(function () { aim = Math.max(aim, 68); }, 450);
      setTimeout(finish, 3400);
    }
  } else {
    doc.classList.add('load-done');
  }

  /* Обработка прокрутки: один расчёт на кадр, только transform */
  var gauge = $('gauge'), gFill = $('gaugeFill'), hdr = $('hdr'), dock = $('dock'),
      para = document.querySelector('[data-parallax]'),
      queued = false, solid = false, docked = false, paraH = 0;

  if (gauge) {
    for (var t = 0; t < 22; t++) {
      var m = document.createElement('i');
      m.style.top = (t / 21 * 100) + '%';
      if (t % 5 === 0) m.style.width = '15px';
      gauge.appendChild(m);
    }
  }

  var measure = function () { paraH = para ? para.offsetHeight : 0; };
  var frame = function () {
    queued = false;
    var y = window.scrollY,
        max = doc.scrollHeight - window.innerHeight,
        p = max > 0 ? y / max : 0;

    if (gFill) gFill.style.transform = 'scaleY(' + p + ')';

    if (hdr) {
      var s = y > 40;
      if (s !== solid) { solid = s; hdr.classList.toggle('solid', s); }
    }
    if (dock) {
      var d = y > window.innerHeight * .6;
      if (d !== docked) { docked = d; dock.classList.toggle('on', d); }
    }
    if (para && !reduce && y < paraH) para.style.transform = 'translate3d(0,' + (y * .16) + 'px,0)';
  };
  var onScroll = function () { if (!queued) { queued = true; requestAnimationFrame(frame); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', function () { measure(); onScroll(); });
  measure(); frame();

  /* Появление блоков и счётчик лет */
  var countEl = document.querySelector('[data-count]');
  var counted = false;
  var countUp = function () {
    if (!countEl || counted || reduce) return;
    counted = true;
    var to = parseInt(countEl.dataset.count, 10), t0 = 0;
    (function run(ts) {
      if (!t0) t0 = ts;
      var k = Math.min((ts - t0) / 1200, 1), e = 1 - Math.pow(1 - k, 4);
      countEl.textContent = Math.round(e * to);
      if (k < 1) requestAnimationFrame(run); else countEl.textContent = to;
    })(0);
  };

  var reveal = document.querySelectorAll('.rv, .l');
  if (reduce || !('IntersectionObserver' in window)) {
    [].forEach.call(reveal, function (el) { el.classList.add('in'); });
  } else {
    if (countEl) countEl.textContent = '0';
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        io.unobserve(e.target);
        if (e.target.contains(countEl)) countUp();
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: .15 });
    [].forEach.call(reveal, function (el) { io.observe(el); });
  }

  /* Блокировка прокрутки с сохранением позиции */
  var lockY = 0, locked = false;
  var lockScroll = function (on) {
    if (on === locked) return;
    locked = on;
    if (on) {
      lockY = window.scrollY;
      var sw = window.innerWidth - doc.clientWidth;
      document.body.style.position = 'fixed';
      document.body.style.top = (-lockY) + 'px';
      document.body.style.left = '0';
      document.body.style.right = '0';
      document.body.style.paddingRight = sw + 'px';
    } else {
      document.body.style.position = '';
      document.body.style.top = '';
      document.body.style.left = '';
      document.body.style.right = '';
      document.body.style.paddingRight = '';
      window.scrollTo(0, lockY);
    }
  };

  /* Меню */
  var burger = $('burger'), sheet = $('sheet');
  var setSheet = function (open) {
    if (!sheet) return;
    sheet.classList.toggle('on', open);
    sheet.setAttribute('aria-hidden', open ? 'false' : 'true');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    burger.setAttribute('aria-label', open ? 'Закрыть меню' : 'Открыть меню');
    lockScroll(open);
  };
  if (burger && sheet) {
    burger.addEventListener('click', function () { setSheet(!sheet.classList.contains('on')); });
    [].forEach.call(sheet.querySelectorAll('a'), function (a) {
      a.addEventListener('click', function () { setSheet(false); });
    });
  }

  /* Полноэкранный просмотр фотографий */
  var lb = $('lb'), lbImg = $('lbImg'), lbIdx = $('lbIdx'), lbTitle = $('lbTitle'),
      shots = [], cur = 0;

  var showShot = function (i) {
    if (!shots.length) return;
    cur = (i + shots.length) % shots.length;
    lb.classList.remove('ready');
    lbIdx.textContent = ('0' + (cur + 1)).slice(-2) + ' / ' + ('0' + shots.length).slice(-2);
    lbImg.alt = (lbTitle.textContent || 'Объект') + ', фото ' + (cur + 1);
    var pre = new Image();
    pre.onload = function () { lbImg.src = pre.src; lb.classList.add('ready'); };
    pre.onerror = function () { lb.classList.add('ready'); };
    pre.src = shots[cur];
  };
  var openLb = function (list, title, i) {
    if (!lb || !list || !list.length) return;
    shots = list;
    lbTitle.textContent = title || '';
    lb.classList.add('on');
    lockScroll(true);
    showShot(i || 0);
    $('lbX').focus();
  };
  var closeLb = function () { if (lb) { lb.classList.remove('on'); lockScroll(false); } };

  if (lb) {
    $('lbX').addEventListener('click', closeLb);
    $('lbPrev').addEventListener('click', function () { showShot(cur - 1); });
    $('lbNext').addEventListener('click', function () { showShot(cur + 1); });
    lb.addEventListener('click', function (e) {
      if (e.target === lb || e.target.className === 'lb__fig') closeLb();
    });
  }

  addEventListener('keydown', function (e) {
    if (lb && lb.classList.contains('on')) {
      if (e.key === 'Escape') closeLb();
      if (e.key === 'ArrowLeft') showShot(cur - 1);
      if (e.key === 'ArrowRight') showShot(cur + 1);
      return;
    }
    if (e.key === 'Escape' && sheet && sheet.classList.contains('on')) { setSheet(false); burger.focus(); }
  });

  /* Галереи объектов задаются на странице в window.GALLERIES */
  var GAL = window.GALLERIES || {};
  [].forEach.call(document.querySelectorAll('[data-gal]'), function (el) {
    var g = GAL[el.dataset.gal];
    if (!g) return;
    el.addEventListener('click', function () { openLb(g.imgs, g.title, 0); });
  });

  /* Лента объектов на главной */
  var rail = $('rail');
  if (rail && window.SHOTS) {
    var wIdx = $('wIdx'), wBar = $('wBar'), wPrev = $('wPrev'), wNext = $('wNext'),
        LIST = window.SHOTS, step2 = 320;

    LIST.forEach(function (src, i) {
      var f = document.createElement('figure');
      f.className = 'shot';
      f.tabIndex = 0;
      f.setAttribute('role', 'button');
      f.setAttribute('aria-label', 'Открыть объект ' + (i + 1));
      var box = document.createElement('div');
      box.className = 'shot__img';
      var img = new Image();
      img.src = src;
      img.alt = 'Объект Траектории № ' + (i + 1);
      img.decoding = 'async';
      if (i > 2) img.loading = 'lazy';
      box.appendChild(img);
      var n = document.createElement('figcaption');
      n.className = 'shot__n';
      n.textContent = ('0' + (i + 1)).slice(-2);
      f.appendChild(box); f.appendChild(n);
      f.addEventListener('click', function () { if (dragged < 7) openLb(LIST, 'Объекты Траектории', i); });
      f.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openLb(LIST, 'Объекты Траектории', i); }
      });
      rail.appendChild(f);
    });

    var remeasure = function () {
      var card = rail.firstElementChild;
      if (card) step2 = card.getBoundingClientRect().width + parseFloat(getComputedStyle(rail).columnGap || 0);
    };
    remeasure();
    addEventListener('resize', remeasure);

    var railQueued = false;
    var railSync = function () {
      railQueued = false;
      var max = rail.scrollWidth - rail.clientWidth,
          p = max > 0 ? rail.scrollLeft / max : 0,
          i = Math.min(LIST.length, Math.round(rail.scrollLeft / step2) + 1);
      wIdx.innerHTML = '<b>' + ('0' + i).slice(-2) + '</b><span> / ' + LIST.length + '</span>';
      wBar.style.transform = 'scaleX(' + (.12 + p * .88) + ')';
      wPrev.disabled = rail.scrollLeft < 4;
      wNext.disabled = max - rail.scrollLeft < 4;
    };
    rail.addEventListener('scroll', function () {
      if (!railQueued) { railQueued = true; requestAnimationFrame(railSync); }
    }, { passive: true });
    wPrev.addEventListener('click', function () { rail.scrollBy({ left: -step2, behavior: reduce ? 'auto' : 'smooth' }); });
    wNext.addEventListener('click', function () { rail.scrollBy({ left: step2, behavior: reduce ? 'auto' : 'smooth' }); });
    rail.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') { e.preventDefault(); wPrev.click(); }
      if (e.key === 'ArrowRight') { e.preventDefault(); wNext.click(); }
    });
    railSync();

    var dragging = false, startX = 0, startL = 0, dragged = 0, pending = null, dragRaf = 0;
    rail.addEventListener('pointerdown', function (e) {
      if (e.pointerType !== 'mouse') return;
      dragging = true; dragged = 0; startX = e.clientX; startL = rail.scrollLeft;
      rail.classList.add('drag');
    });
    addEventListener('pointermove', function (e) {
      if (!dragging) return;
      pending = startL - (e.clientX - startX);
      dragged = Math.abs(e.clientX - startX);
      if (!dragRaf) dragRaf = requestAnimationFrame(function () {
        dragRaf = 0;
        if (pending !== null) rail.scrollLeft = pending;
      });
    }, { passive: true });
    addEventListener('pointerup', function () {
      if (!dragging) return;
      dragging = false; pending = null; rail.classList.remove('drag');
      setTimeout(function () { dragged = 0; }, 60);
    });
  }
  var dragged = 0;

  /* Курсор и магнитные кнопки */
  if (fine && !reduce) {
    var ring = $('cur'), dot = $('curDot');
    if (ring && dot) {
      var mx = innerWidth / 2, my = innerHeight / 2, rx = mx, ry = my;

      addEventListener('pointermove', function (e) {
        if (!doc.classList.contains('has-cur')) {
          rx = mx = e.clientX; ry = my = e.clientY;
          doc.classList.add('has-cur');
        }
        mx = e.clientX; my = e.clientY;
        dot.style.transform = 'translate3d(' + mx + 'px,' + my + 'px,0)';
      }, { passive: true });

      (function ride() {
        rx += (mx - rx) * .17;
        ry += (my - ry) * .17;
        ring.style.transform = 'translate3d(' + rx + 'px,' + ry + 'px,0)';
        requestAnimationFrame(ride);
      })();

      addEventListener('pointerover', function (e) {
        var overRail = e.target.closest && e.target.closest('.rail');
        var overHot = e.target.closest && e.target.closest('a,button,.shot,.card');
        ring.classList.toggle('grab', !!overRail);
        ring.classList.toggle('hot', !!overHot && !overRail);
        dot.classList.toggle('hide', !!overRail);
      }, { passive: true });

      [].forEach.call(document.querySelectorAll('.magnet'), function (el) {
        el.addEventListener('pointermove', function (e) {
          var b = el.getBoundingClientRect();
          el.style.transform = 'translate3d(' + ((e.clientX - b.left - b.width / 2) * .22) + 'px,' +
                               ((e.clientY - b.top - b.height / 2) * .35) + 'px,0)';
        });
        el.addEventListener('pointerleave', function () { el.style.transform = ''; });
      });
    }
  }

  /* Печатная машинка. Фразы задаются на странице в window.PHRASES */
  var typed = $('typed'), ghost = $('ghost');
  if (typed && ghost && window.PHRASES) {
    var P = window.PHRASES;
    ghost.textContent = P.reduce(function (a, b) { return b.length > a.length ? b : a; }, '');
    if (reduce) {
      typed.textContent = P[0];
    } else {
      var pi = 0, ci = 0, del = false;
      (function type() {
        var w = P[pi];
        typed.textContent = w.slice(0, ci);
        if (!del) {
          if (ci < w.length) { ci++; setTimeout(type, 58); }
          else { del = true; setTimeout(type, 1900); }
        } else {
          if (ci > 0) { ci--; setTimeout(type, 26); }
          else { del = false; pi = (pi + 1) % P.length; setTimeout(type, 260); }
        }
      })();
    }
  }

  /* Логотипы партнёров.
     Положите файл в assets/img/partners/<slug>.svg или .png —
     он появится в карточке сам. Пока файла нет, место остаётся пустым. */
  [].forEach.call(document.querySelectorAll('[data-logo]'), function (el) {
    var src = el.getAttribute('data-logo');
    var probe = new Image();
    probe.onload = function () { el.src = src; el.classList.add('on'); };
    probe.src = src;
  });

  /* Форма заявки.
     FORM_ENDPOINT: адрес обработчика. Пока пуст, заявка уходит письмом
     через почтовую программу. Впишите сюда адрес своего обработчика
     или сервиса приёма форм, и отправка пойдёт напрямую. */
  var FORM_ENDPOINT = '';
  var MAIL_TO = 'info@traektoriya.pro';

  var urlProj = new URLSearchParams(location.search).get('p');

  var bindForm = function (form) {
    var wrap = form.parentNode;
    var note = form.querySelector('[data-note]');
    var doneEl = wrap.querySelector('[data-done]');
    var policy = form.querySelector('[data-policy]');
    var field = function (n) { return form.querySelector('[name="' + n + '"]'); };

    var proj = field('proj');
    if (urlProj && proj) proj.value = urlProj;

    if (policy) {
      policy.addEventListener('click', function (e) {
        e.preventDefault();
        alert('Разместите здесь ссылку на политику обработки персональных данных.');
      });
    }

    var warn = function (msg, el) {
      if (note) { note.textContent = msg; note.classList.add('form__note--warn'); }
      if (el) el.focus();
    };

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var tel = field('tel'), ok = field('ok');

      if (!tel.value.trim()) return warn('Укажите телефон: без него мы не сможем перезвонить.', tel);
      if (ok && !ok.checked) return warn('Нужно согласие на обработку данных.', ok);

      var val = function (n) { var f = field(n); return f ? f.value.trim() : ''; };
      var d = {
        name: val('name'), tel: tel.value.trim(), mail: val('mail'),
        kind: val('kind'), proj: val('proj'), msg: val('msg')
      };

      var done = function () {
        form.classList.add('hide');
        var box = form.closest('.modal__in');
        if (box) box.classList.add('sent');
        if (!doneEl) return;
        doneEl.classList.add('on');
        if (!form.closest('.modal')) {
          doneEl.scrollIntoView({ block: 'center', behavior: reduce ? 'auto' : 'smooth' });
        }
      };

      if (FORM_ENDPOINT) {
        fetch(FORM_ENDPOINT, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(d)
        }).then(done).catch(function () {
          warn('Не удалось отправить. Позвоните нам или напишите на почту.');
        });
        return;
      }

      var body = [
        'Имя: ' + (d.name || 'не указано'),
        'Телефон: ' + d.tel,
        'Почта: ' + (d.mail || 'не указана'),
        'Направление: ' + d.kind,
        'Проект: ' + (d.proj || 'не выбран'),
        '',
        d.msg
      ].join('\n');
      location.href = 'mailto:' + MAIL_TO +
        '?subject=' + encodeURIComponent('Заявка с сайта: ' + d.kind) +
        '&body=' + encodeURIComponent(body);
      setTimeout(done, 600);
    });
  };

  [].forEach.call(document.querySelectorAll('form[data-form]'), bindForm);

  /* Всплывающее окно заявки */
  var modal = $('modal');
  if (modal) {
    var mForm = modal.querySelector('form[data-form]');
    var mDone = modal.querySelector('[data-done]');
    var mTitle = $('modalTitle'), mLead = $('modalLead'), mKicker = $('modalKicker');
    var lastFocus = null;

    var setModal = function (open) {
      modal.classList.toggle('on', open);
      modal.setAttribute('aria-hidden', open ? 'false' : 'true');
      lockScroll(open);
      if (open) {
        var first = modal.querySelector('input,select,textarea,button');
        if (first) first.focus();
      } else if (lastFocus) {
        lastFocus.focus();
        lastFocus = null;
      }
    };

    var openModal = function (opts) {
      opts = opts || {};
      lastFocus = document.activeElement;
      mForm.classList.remove('hide');
      mDone.classList.remove('on');
      var box = modal.querySelector('.modal__in');
      if (box) box.classList.remove('sent');
      if (mKicker) mKicker.textContent = opts.kicker || 'Заявка';
      if (mTitle) mTitle.textContent = opts.title || 'Обсудим ваш проект';
      if (mLead) mLead.textContent = opts.lead ||
        'Оставьте телефон, перезвоним и уточним задачу. Это ни к чему не обязывает.';
      var pf = mForm.querySelector('[name="proj"]');
      if (pf) pf.value = opts.proj || '';
      var kf = mForm.querySelector('[name="kind"]');
      if (kf && opts.kind) {
        [].forEach.call(kf.options, function (o) { if (o.value === opts.kind) kf.value = opts.kind; });
      }
      var nt = mForm.querySelector('[data-note]');
      if (nt) nt.classList.remove('form__note--warn');
      setModal(true);
    };

    [].forEach.call(modal.querySelectorAll('[data-modal-close]'), function (el) {
      el.addEventListener('click', function () { setModal(false); });
    });

    addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && modal.classList.contains('on')) setModal(false);
    });

    /* Любая ссылка на страницу заявки, почта и кнопка «Позвонить»
       на компьютере открывают окно вместо перехода. На телефоне
       «Позвонить» остаётся звонком, почта — письмом. */
    var onZayavka = /zayavka\.html/.test(location.pathname);

    document.addEventListener('click', function (e) {
      var t = e.target.closest ? e.target.closest('a[href],button[data-gal]') : null;
      if (!t || !t.getAttribute) return;
      var href = t.getAttribute('href') || '';

      if (href.indexOf('zayavka.html') === 0 && !onZayavka) {
        e.preventDefault();
        var q = href.split('?p=')[1];
        openModal({ proj: q ? decodeURIComponent(q.replace(/\+/g, ' ')) : '' });
        return;
      }
      if (href.indexOf('mailto:') === 0) {
        e.preventDefault();
        openModal({
          kicker: 'Письмо',
          title: 'Напишите нам',
          lead: 'Опишите задачу — ответим на почту или перезвоним, как удобнее.'
        });
        return;
      }
      if (href.indexOf('tel:') === 0 && fine && t.classList.contains('cta')) {
        e.preventDefault();
        openModal({
          kicker: 'Обратный звонок',
          title: 'Перезвоним вам',
          lead: 'Оставьте номер и удобное время — наберём сами. Или позвоните сразу: ' + t.textContent.trim() + '.'
        });
      }
    });
  }
})();
