// Show popup when page loads
window.onload = function() {
    document.getElementById('welcomePopup').style.display = 'flex';
};

// Close popup when clicking X
document.querySelector('.close-btn').addEventListener('click', function() {
    document.getElementById('welcomePopup').style.display = 'none';
});

// Close popup when clicking outside content
window.addEventListener('click', function(event) {
    const popup = document.getElementById('welcomePopup');
    if (event.target === popup) {
        popup.style.display = 'none';
    }
});