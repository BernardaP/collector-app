M.AutoInit();
// document.addEventListener('DOMContentLoaded', function() {
//     var elems = document.querySelectorAll('.sidenav');
//     var instances = M.Sidenav.init(elems);
// });

// DatePicker

const dateEl = document.getElementById('id_date');
M.Datepicker.init(dateEl, {
  format: 'yyyy-mm-dd',
  defaultDate: new Date(),
  setDefaultDate: true,
  autoClose: true
});

// TimePicker
const timeEl = document.getElementById('id_time');
M.Timepicker.init(timeEl, {
  twelveHour: true,
  defaultTime: 'now',
  autoClose: true
});
