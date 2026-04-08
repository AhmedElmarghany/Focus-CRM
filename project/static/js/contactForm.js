// Initializing the Emailjs library
(function () {
  emailjs.init({
    publicKey: "5pYQt3u5z5lhEMQwp",
  });
})();

const form = document.getElementById("contact-form");

form.addEventListener("submit", function (e) {
  e.preventDefault();

  // Inject random submission id in form
  // 1. Generate the random ID
  const submissionId = Math.random().toString(12).slice(2, 12);

  // 2. Create a hidden input and append it to the form
  const hidden_sub_Input = document.createElement("input");
  hidden_sub_Input.type = "hidden";
  hidden_sub_Input.name = "submission_id"; // Matches {{submission_id}} in email template
  hidden_sub_Input.value = submissionId;
  form.appendChild(hidden_sub_Input);

  // Inject Instant DateTime in form
  // 1. Populate the hidden time field
  const now = new Date();
  const formattedTime = now.toLocaleString(); // Or format as needed

  // 2. Create a hidden input and append it to the form
  const hiddenInput = document.createElement("input");
  hiddenInput.type = "hidden";
  hiddenInput.name = "timestamp"; // Matches {{timestamp}} in email template
  hiddenInput.value = formattedTime;
  form.appendChild(hiddenInput);

  const btn = this.querySelector(".ct-submit-btn");
  btn.textContent = "Sending…";
  btn.disabled = true;

  // Send Form
  emailjs.sendForm("service_focus", "Focus-CRM", form).then(
    () => {
      console.log("success");
      document.getElementById("form-content").style.display = "none";
      const success = document.getElementById("ct-success");
      success.style.display = "flex";
    },
    (error) => {
      console.log("FAILED...", error);
    },
  );
});
