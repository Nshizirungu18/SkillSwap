// =====================
// SkillSwap JS Structure
// =====================

// DOM Elements
const loginBtn = document.getElementById("openLogin");
const signupBtn = document.getElementById("openSignup");
const matchBtn = document.querySelector(".skill-match .btn-primary");
const matchResult = document.querySelector(".match-result");
const contactForm = document.querySelector(".form");

// =====================
// 1. Authentication
// =====================
// For now, we’ll just mock modal behavior
loginBtn.addEventListener("click", () => {
  alert("Login modal would open here.");
});

signupBtn.addEventListener("click", () => {
  alert("Signup modal would open here.");
});

// =====================
// 2. Skill Match System
// =====================
matchBtn.addEventListener("click", () => {
  const role = document.querySelector("input[name='role']:checked")?.value;
  const lesson = document.getElementById("lesson").value.trim();
  const level = document.getElementById("skill-level").value;
  const availability = document.getElementById("availability").value;

  if (!role || !lesson || !availability) {
    alert("⚠ Please fill in all fields before searching.");
    return;
  }

  // Mock matching result
  matchResult.innerHTML = `
    <h3>🎉 Match Found!</h3>
    <p><strong>${role === "teach" ? "Instructor" : "Student"}:</strong> You</p>
    <p><strong>${role === "teach" ? "Student" : "Instructor"}:</strong> Alex P. (${lesson})</p>
    <p><strong>Skill Level:</strong> ${level}</p>
    <p><strong>Proposed Time:</strong> ${new Date(availability).toLocaleString()}</p>
    <p class="note">💡 Don’t agree? The system will suggest another time.</p>
  `;
  matchResult.style.display = "block";
});

// =====================
// 3. Pricing Buttons
// =====================
document.querySelectorAll(".pricing-section .btn").forEach(button => {
  button.addEventListener("click", () => {
    alert(`You selected: ${button.closest(".card").querySelector(".plan-title").textContent}`);
  });
});

// =====================
// 4. Contact Form
// =====================
contactForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const message = document.getElementById("message").value.trim();

  if (!name || !email || !message) {
    alert("⚠ Please fill out all fields.");
    return;
  }

  alert(`✅ Thank you ${name}, your message has been sent!`);
  contactForm.reset();
});

// =====================
// 5. Smooth Scroll
// =====================
document.querySelectorAll("a[href^='#']").forEach(anchor => {
  anchor.addEventListener("click", function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      target.scrollIntoView({ behavior: "smooth" });
    }
  });
});
