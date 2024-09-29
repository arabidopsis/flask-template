;(function () {
  // turn Notyf into a more toastr like interface
  if (!window.Notyf) {
    console.log('no Notyf!')
    return
  }
  const notyf = new window.Notyf({
    position: { x: "right", y: "top" },
    types: [
      {
        type: "success-toastr",
        icon: {
          className: "fas fa-check",
          tagName: "i",
          color: "var(--bs-light)",
        },
        background: "var(--bs-success)",
      },
      {
        type: "error-toastr",
        icon: {
          className: "fas fa-bomb",
          tagName: "i",
          color: "var(--bs-light)",
        },
        background: "var(--bs-danger)",
      },
      {
        type: "info",
        icon: {
          className: "fas fa-info-circle",
          tagName: "i",
          color: "var(--bs-light)",
        },
        background: "var(--bs-info)",
      },
      {
        type: "warning",
        icon: {
          className: "fas fa-exclamation-triangle",
          tagName: "i",
          color: "var(--bs-light)",
        },
        background: "var(--bs-warning)",
      },
    ],
  })
  function open(type, message, options) {
    return notyf.open({ type, message, ...options })
  }
  window.toastr = {
    notyf: notyf,
    success: function (msg, options = {}) {
      return open("success-toastr", msg, options)
    },
    error: function (msg, options = {}) {
      return open("error-toastr", msg, options)
    },
    warning: function (msg, options = {}) {
      return open("warning", msg, options)
    },
    info: function (msg, options = {}) {
      return open("info", msg, options)
    },
    dismiss: function (notification) {
      return notyf.dismiss(notification)
    },
    dismissAll: function () {
      return notyf.dismissAll()
    },
  }
})()
