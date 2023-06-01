// Update the minimum date for the end date field based on the selected start date
function updateEndDateMinDate(startDate) {
    var endDateField = document.getElementById('end_date');
    endDateField.min = startDate;
  }
  
  // Disable the dates before the current date in the date picker
  function disablePastDates() {
    var today = new Date().toISOString().split('T')[0];
    var dateInputs = document.querySelectorAll('input[type="date"]');
    
    for (var i = 0; i < dateInputs.length; i++) {
      var dateInput = dateInputs[i];
      dateInput.min = today;
    }
  }
  
  // Call the disablePastDates function when the page is loaded
  window.addEventListener('DOMContentLoaded', disablePastDates);
  