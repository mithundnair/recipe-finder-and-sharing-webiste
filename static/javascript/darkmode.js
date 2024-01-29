    console.log('darkmode.js is running!');

    
    const darkModeToggle = document.getElementById('darkModeToggle');

      darkModeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        const isDarkMode = document.body.classList.contains('dark-mode');
        localStorage.setItem('darkMode', isDarkMode);
      });

      // Check local storage for user's dark mode preference
      const savedDarkMode = localStorage.getItem('darkMode');
      if (savedDarkMode === 'true') {
        document.body.classList.add('dark-mode');
      }