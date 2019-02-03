/**
 * submitForm - Submit ajax post requests
 * @param {Object} event
 * @param {String} url - url of request to make
 * @param {Object} form - DOM object of form
 * @param {Object} spinner - DOM object for button to add spinner to
 * @param {Object} options - Extra options for headers and redirect URL
 * 							- headers {Object} - request headers to send
 * 							- redirect {String} - Redirect url to visit after successful request
 * @param {Function} callback - Function to call after request is done.
 * 								Will recieve 2 arguments, error and response
 */
function submitForm (event, url, form, spinner, options, callback) {
	if (event){
		event.preventDefault();
	}
	var content = addSpinner(spinner)
	
	if(options){
		var redirect = options.redirect
		var headers = options.headers
	}

	form.find('.prompt').remove();
	form.find('.error').removeClass('error');

	var formData = new FormData(form[0]);
	$.ajax({
		url: url,
		type: 'POST',
		data: formData,
		beforeSend: function(req) {
			headers && Object.keys(headers).forEach(header => {
				req.setRequestHeader(header, headers[header])
			})
			req.setRequestHeader('X-CSRFToken', getCsrfToken())
		},
		contentType: false,
		processData: false,
		error: function (response) {
			removeSpinner(spinner, content)		
			return callback(response.errors)
		},
		success: function(response) {
			removeSpinner(spinner, content)
			if (!response.errors) {
				if (redirect) {
					window.location.href = redirect
					return true
				}
				return callback(null, response)
			} else {
				renderErrors(response.errors, form)
				return callback(response.errors)
			}
		},
	})
}

function getCsrfToken () {
	if ($('[name=csrfmiddlewaretoken]')) {
		return $('[name=csrfmiddlewaretoken]').val()
	}
	return document.cookie.indexOf('csrftoken=')[1].split(';')[0]
}

function addSpinner(spinner) {
	if (spinner) {
		spinner.prop('disabled', true)
		return showSpinner(spinner)
	}
	return spinner
}

function removeSpinner(spinner, content) {
	if (spinner) {
		hideSpinner(spinner, content)
		return spinner.prop('disabled', false)
	}
	return spinner
}

function renderErrors(errors, form) {
	var error = ''
	for (var key in errors) {
		console.log(key)
		error = errors[key][0];
		form.find('.field').each(function() {
			var $field = $(this);
			if ($field.find('input[name*="' + key + '"], select[name*="' + key + '"], textarea[name*="' + key + '"]').length) {
				$field.addClass('error');
				$field.append('<div class="ui basic red pointing prompt label transition visible">' + error + '</div>')
			}
		});
	}
	if (errors.hasOwnProperty('__all__')){
		form.append('<center><div style="margin-top: 1.5rem" class="ui basic red prompt label transition visible non-form-error">' + error + '</div></center>')
	}
}
