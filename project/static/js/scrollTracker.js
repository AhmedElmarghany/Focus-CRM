(function () {
  // All nav links that point to a section
  const navLinks = document.querySelectorAll(
    '.navbar-nav .nav-link[href^="/#"]',
  );

  // Build a map: sectionId → navLink
  const sectionMap = new Map();
  navLinks.forEach((link) => {
    const id = link.getAttribute("href").replace("/#", "");
    if (id) sectionMap.set(id, link);
  });

  function setActive(activeLink) {
    navLinks.forEach((link) => link.classList.remove("active"));
    if (activeLink) activeLink.classList.add("active");
  }

  // ── Click: set active immediately, let the browser scroll ──────
  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      setActive(link);
    });
  });

  // ── Scroll: IntersectionObserver — most reliable approach ───────
  const observerOptions = {
    root: null, // viewport
    rootMargin: "-20% 0px -70% 0px", // trigger when section is in the top 30% band
    threshold: 0,
  };

  let activeFromClick = null;
  let clickTimeout = null;

  // After a click, give the browser ~800ms to finish scrolling
  // before the observer takes over again
  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      activeFromClick = link;
      clearTimeout(clickTimeout);
      clickTimeout = setTimeout(() => {
        activeFromClick = null;
      }, 800);
    });
  });

  const observer = new IntersectionObserver((entries) => {
    if (activeFromClick) return; // don't fight a recent click

    // Among all currently intersecting sections, pick the topmost one
    const intersecting = entries
      .filter((e) => e.isIntersecting)
      .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);

    if (intersecting.length > 0) {
      const id = intersecting[0].target.id;
      const link = sectionMap.get(id);
      if (link) setActive(link);
    }
  }, observerOptions);

  // Observe every section that has a matching nav link
  sectionMap.forEach((_, id) => {
    const el = document.getElementById(id);
    if (el) observer.observe(el);
  });

  // ── Edge case: highlight "Home" when scrolled to the very top ───
  const homeLink = document.querySelector('.navbar-nav .nav-link[href="/#"]');
  if (homeLink) {
    window.addEventListener(
      "scroll",
      () => {
        if (activeFromClick) return;
        if (window.scrollY < 80) setActive(homeLink);
      },
      { passive: true },
    );
  }
})();
