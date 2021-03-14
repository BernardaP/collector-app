M.AutoInit();


// DatePicker

const dateEl = document.getElementById('id_date');
M.Datepicker.init(dateEl, {
  format: 'yyyy-mm-dd',
  defaultDate: new Date(),
  setDefaultDate: true,
  autoClose: false
});

// TimePicker
const timeEl = document.getElementById('id_time');
M.Timepicker.init(timeEl, {
  twelveHour: false,
  defaultTime: 'now',
  autoClose: false
});
