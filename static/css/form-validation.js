$(function() {
    $("form[name='registration']").validate({
      rules: {
        telefone1: {
          required: true
        }
      },
      messages: {
        telefone1: {
          required: "This field is required!"
        }
      },
      errorClass: "error", // add "error" class to invalid elements
      highlight: function(element, errorClass, validClass) {
        $(element).addClass(errorClass).removeClass(validClass);
        if ($(element).hasClass("phone-group")) {
          $(element).addClass("error");
        }
      },
      unhighlight: function(element, errorClass, validClass) {
        $(element).removeClass(errorClass).addClass(validClass);
        if ($(element).hasClass("phone-group")) {
          $(element).removeClass("error");
        }
      },
      submitHandler: function(form) {
        form.submit();
      }
    });
  });

    //Telefone fixo
    jQuery.validator.addMethod('telefone', function (value, element) {
        value = value.replace("(", "");
        value = value.replace(")", "");
        value = value.replace("-", "");
        value = value.replace(" ", "").trim();
        if (value == '0000000000') {
            return (this.optional(element) || false);
        } else if (value == '00000000000') {
            return (this.optional(element) || false);
        }
        if (["00", "01", "02", "03", , "04", , "05", , "06", , "07", , "08", "09", "10"].indexOf(value.substring(0, 2)) != -1) {
            return (this.optional(element) || false);
        }
        if (value.length < 10 || value.length > 11) {
            return (this.optional(element) || false);
        }
        if (["1", "2", "3", "4","5"].indexOf(value.substring(2, 3)) == -1) {
            return (this.optional(element) || false);
        }
        return (this.optional(element) || true);
    }, 'Inform a valid phone'); 