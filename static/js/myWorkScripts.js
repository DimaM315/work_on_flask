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

	/*$.ajax({
		url:'articles.php',
		type:'GET',
		data:{
			title: title,
			text: text
		},
		success:function(response, status){
			if(response > 0){ // ответ - '2' - положительный, текст - отрицательный
				window.location.href = "http://bs";
			}else{
				alert(response);
			};
		}
	})*/
});

$('#save').on('click', function(){
	var title = document.getElementById('title').value; 
	var text = document.getElementById('text').value;

	/*$.ajax({
		url:'articles.php',
		type:'GET',
		data:{
			save: 1,
			work: title+'-!!!-'+text
		},
		success:function(response, status){
			if(response === 'save'){ // ответ - 'save' - положительный, другое - отрицательный
				window.location.href = "http://bs";
			}else{
				alert(response);
			};
		}
	})*/
});