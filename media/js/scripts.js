$(function(){
	$("#btnBusca").click(function(){
		$.ajax({
			type: "POST",
			data: $("#frmBusca").serialize(),
			url: "busca/",
			success: function(data){
				$("#resultado").html(data);
			}
		});
	});
});
