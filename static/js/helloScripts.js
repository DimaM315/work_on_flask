$('#login').on('click', function(){
	$('#form_auto').css('transform','rotateY(0deg)');
	$('#form_reg').css('transform','rotateY(90deg)');
});


$('#reg').on('click', function(){
	$('#form_reg').css('transform','rotateY(0deg)');
	$('#form_auto').css('transform','rotateY(90deg)');
});


$('#enter').on('click', function(){
	var pass = document.getElementById('auto_pass').value; 
	var nick = document.getElementById('auto_login').value;

	$.ajax({
		url:'enter.php',
		type:'GET',
		data:{
			nick: nick,
			pass: pass
		},
		success:function(response, status){
			if(response > 0){ // ответ - id пользователя, либо строка
				window.location.href = "http://bs";
			}else{
				alert(response);
			};
		}
	})
});

$('#reg_order').on('click', function(){
	var pass = document.getElementById('reg_pass').value; 
	var nick = document.getElementById('reg_login').value;
	var name = document.getElementById('reg_name').value;
	var surname = document.getElementById('reg_surname').value;

	$.ajax({
		url:'enter.php',
		type:'GET',
		data:{
			reg:'reg',
			nick: nick,
			pass: pass,
			name: name,
			surname: surname
		},
		success:function(response, status){
			if(response > 1){ // ответ - 2, при удачной регистрации
				alert("Вы можите войти в систему. Логин - "+nick+". Пороль - "+pass);
			}else{
				alert(response+1);
			};
		}
	})
	$('#form_auto').css('transform','rotateY(0deg)');
	$('#form_reg').css('transform','rotateY(90deg)');
})