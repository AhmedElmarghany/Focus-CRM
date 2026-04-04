// password visibility
function togglePw(inputId, iconId) {
  const pw = document.getElementById(inputId);
  const icon = document.getElementById(iconId);
  const isHidden = pw.type === "password";
  pw.type = isHidden ? "text" : "password";
  icon.innerHTML = isHidden
    ? '<path d="M17.94 17.94A10.07 10.07 0 0112 20c-7 0-11-8-11-8a18.45 18.45 0 015.06-5.94M9.9 4.24A9.12 9.12 0 0112 4c7 0 11 8 11 8a18.5 18.5 0 01-2.16 3.19m-6.72-1.07a3 3 0 11-4.24-4.24"/><line x1="1" y1="1" x2="23" y2="23"/>'
    : '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>';
}
// Strength meter
function updateStrength(val) {
  let score = 0;
  if (val.length >= 8) score++;
  if (/[A-Z]/.test(val)) score++;
  if (/[0-9]/.test(val)) score++;
  if (/[^A-Za-z0-9]/.test(val)) score++;

  const colors = ["", "#c9373d", "#b07a10", "#416791", "#2a7d56"];
  const labels = ["", "Weak", "Fair", "Good", "Strong"];
  const empty = "var(--secondary)";

  ["s1", "s2", "s3", "s4"].forEach((id, i) => {
    document.getElementById(id).style.background =
      val.length === 0 ? empty : i < score ? colors[score] : empty;
  });

  const lbl = document.getElementById("strength-label");
  lbl.textContent = val.length === 0 ? "" : labels[score] || "";
  lbl.style.color = val.length === 0 ? "" : colors[score];
}
// Matching check
function checkMatch() {
  const pw = document.getElementById("password").value;
  const conf = document.getElementById("confirm-password").value;
  const ind = document.getElementById("match-indicator");
  const dot = document.getElementById("match-dot");
  const txt = document.getElementById("match-text");
  const inp = document.getElementById("confirm-password");

  if (conf.length === 0) {
    ind.classList.remove("visible");
    inp.classList.remove("is-invalid", "is-valid-match");
    return;
  }

  ind.classList.add("visible");

  if (pw === conf) {
    dot.style.background = "#2a7d56";
    txt.textContent = "Passwords match";
    txt.style.color = "#2a7d56";
    inp.classList.remove("is-invalid");
    inp.classList.add("is-valid-match");
  } else {
    dot.style.background = "var(--destructive)";
    txt.textContent = "Passwords do not match";
    txt.style.color = "var(--destructive)";
    inp.classList.remove("is-valid-match");
    inp.classList.add("is-invalid");
  }
}
