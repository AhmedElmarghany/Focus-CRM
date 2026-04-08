  (function () {
    const AUTO_DISMISS_MS = 4000;
    const ANIM_DURATION_MS = 320;

    function dismissToast(el) {
      if (el.classList.contains('leaving')) return;
      el.classList.add('leaving');
      setTimeout(() => el.remove(), ANIM_DURATION_MS);
    }

    document.querySelectorAll('.toast-msg').forEach(function (toast, idx) {
      // stagger entrance
      toast.style.animationDelay = (idx * 80) + 'ms';

      // auto-dismiss after progress bar duration
      const timer = setTimeout(() => dismissToast(toast), AUTO_DISMISS_MS + idx * 80);

      // manual close
      toast.querySelector('.toast-close').addEventListener('click', function () {
        clearTimeout(timer);
        dismissToast(toast);
      });
    });
  })();