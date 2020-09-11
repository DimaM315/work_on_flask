$('#title').on('keyup', function() {
	var titleLength = $(this).val().length;
	if(titleLength > 45){
		$('#error_title').css('display','block');
	}else{
		$('#error_title').css('display','none');
	};
});


$('#text').on('keyup', function() {
	var titleLength = $(this).val().length;
	if(titleLength < 100){
		$('#error_text').css('display','block');
	}else{
		$('#error_text').css('display','none');
	};
});

$('#done').on('click', function(){
	var title = document.getElementById('title').value; 
	var text = document.getElementById('text').value;

	/*var xhr = new XMLHttpRequest();
	xhr.open('POST', '/create_post', false)
	xhr.send([title, text]);
	
	console.log(xhr.status)*/
});

$('#save').on('click', function(){
	var title = document.getElementById('title').value; 
	var text = document.getElementById('text').value;

	var xhr = new XMLHttpRequest();
	xhr.open('POST', '/article/save', true)
	xhr.send([title, text]);
});