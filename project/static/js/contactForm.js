document
  .getElementById("contact-form")
  .addEventListener("submit", function (e) {
    e.preventDefault();
    const btn = this.querySelector(".ct-submit-btn");
    btn.textContent = "Sending…";
    btn.disabled = true;

    setTimeout(() => {
      document.getElementById("form-content").style.display = "none";
      const success = document.getElementById("ct-success");
      success.style.display = "flex";
    }, 900);
  });
