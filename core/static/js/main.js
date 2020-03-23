document.addEventListener("DOMContentLoaded", function() {
    // Task: To color active links and add sronly
    // ------------------------------------------
  
    // Check if actual page is contained in nav menu links
    let navlinks = document.querySelectorAll(".nav-item a");
    let alinks = []; // THE array of links
    navlinks.forEach(item => {
      alinks.push("/" + item.href.split("/")[3]);
    }); // now we have an array "alinks" with each link of nav menu items
  
    // If actual page is contained in nav menu links ("alinks"), then color that link!
    let path = window.location.pathname; // saves current page URL
    if (alinks.includes(path)) {
      document
        .querySelector('.nav-item a[href="' + path + '"]')
        .parentNode.classList.add("active");
      let sronly = '<span class="sr-only">(current)</span>';
      document
        .querySelector('.nav-item a[href="' + path + '"]')
        .insertAdjacentHTML("beforeend", sronly);
    }
});