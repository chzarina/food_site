// Mobile Menu Toggle
document.addEventListener("DOMContentLoaded", () => {
    const mobileMenuToggle = document.querySelector(".mobile-menu-toggle")
    const navMenu = document.querySelector(".nav-menu")
  
    if (mobileMenuToggle && navMenu) {
      mobileMenuToggle.addEventListener("click", () => {
        navMenu.classList.toggle("active")
      })
    }
  
    // Close messages
    const closeButtons = document.querySelectorAll(".close-btn")
    closeButtons.forEach((button) => {
      button.addEventListener("click", function () {
        this.parentElement.style.display = "none"
      })
    })
  
    // Auto hide messages after 5 seconds
    const messages = document.querySelectorAll(".alert")
    messages.forEach((message) => {
      setTimeout(() => {
        message.style.display = "none"
      }, 5000)
    })
  
    // Smooth scrolling for anchor links (if any)
    const anchorLinks = document.querySelectorAll('a[href^="#"]')
    anchorLinks.forEach((link) => {
      link.addEventListener("click", function (e) {
        e.preventDefault()
        const target = document.querySelector(this.getAttribute("href"))
        if (target) {
          target.scrollIntoView({
            behavior: "smooth",
            block: "start",
          })
        }
      })
    })
  
    // Header scroll effect
    const header = document.querySelector(".header")
    if (header) {
      window.addEventListener("scroll", () => {
        if (window.scrollY > 100) {
          header.classList.add("scrolled")
        } else {
          header.classList.remove("scrolled")
        }
      })
    }
  
    // Basic form validation (client-side)
    document.querySelectorAll("form").forEach((form) => {
      form.addEventListener("submit", function (e) {
        const requiredFields = this.querySelectorAll("[required]")
        let isValid = true
  
        requiredFields.forEach((field) => {
          if (!field.value.trim()) {
            field.classList.add("error")
            isValid = false
          } else {
            field.classList.remove("error")
          }
        })
  
        if (!isValid) {
          e.preventDefault() // Prevent form submission if validation fails
          // You might want to show a more user-friendly error message here
          // alert("Please fill in all required fields.");
        }
      })
    })
  })
  