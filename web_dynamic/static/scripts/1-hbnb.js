$(document).ready(function () {
    // Initialize an empty array to store checked Amenity IDs
    const amentiesChecked = [];
  
    // Listen for changes on input checkboxes
    $('input[type="checkbox"]').change(function () {
      const amenityID = $(this).data('id');
  
      if ($(this).is(':checked')) {
        // Add the Amenity ID to the list if the checkbox is checked
        amentiesChecked.push(amenityID);
      } else {
        // Remove the Amenity ID from the list if the checkbox is unchecked
        const index = amentiesChecked.indexOf(amenityID);
        if (index !== -1) {
          amentiesChecked.splice(index, 1);
        }
      }
  
      // Update the h4 tag inside the Amenities div with the list of checked amenities
      $('.Amenities h4').text('Amenities: ' + amentiesChecked.join(', '));
    });
  });
