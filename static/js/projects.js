$(dodument).ready(function(){
    $('form').submit(function(event){
        event.preventDefault()
        form = $("form")

        $.ajax({
            'url':'ajax/rating',
            'type':'POST',
            'data':form.serialize(),
            'success': function(data){
                alert(data['success'])
            },
        })
    })
})