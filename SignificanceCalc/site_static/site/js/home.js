function calculate() {
    var cvVal = $('#control_visitors').val();
    var vvVal = $('#variation_visitors').val();
    var ccVal = $('#control_conversions').val();
    var vcVal = $('#variation_conversions').val();

    if (cvVal === '' || vvVal === '' || ccVal === '' || vcVal === '') {
        alert('Please enter numbers in all control and variation fields.');
        return;
    }
    if (cvVal < 15 || vvVal < 15) {
        alert('There must be at least 15 control trials for this tool to produce any results.');
        return;
    }
    if (ccVal > cvVal || vcVal > vvVal) {
        alert('Numbers of conversions should not be bigger than numbers of visitors');
        return;
    }

    var params = $.param({
        control_visitors: cvVal,
        variation_visitors: vvVal,
        control_conversions: ccVal,
        variation_conversions: vcVal
    });
    var url = window.location.href + 'calculate?' + params;

    $.ajax(url)
        .done(function(data) {
            $('.results').show();
            $('#p_value').text(data.p_value);
            $('#significance').text(data.significance);
            $("html, body").animate({ scrollTop: $(document).height() }, 1000);
        })
        .fail(function(data) {
            console.log(data);
            alert('Sorry. Something went wrong :(');
        });
}
