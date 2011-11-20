$(function(){
	
	$("#btnBusca").click(function(){
		$.ajax({
			type: "POST",
			data: $("#frmBusca").serialize(),
			url: "busca/",
			beforeSend: function(){
				$("#resultado").html("<img style='margin-left: 650px; margin-top: 200px' src='media/images/loader.gif'/>");
			},
			success: function(data){
				$("#resultado").html(data);
			}
		});
	});
	
	$("#btnGerarXml").click(function(){
		window.location = 'xml/';
	});

});