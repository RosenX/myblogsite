window.onload = function(){
	$(".article_show").html( $(".article_show").text());
	//标签页
	var choice_li = getByid('left_menu_choice').getElementsByTagName('li');
	var body = document.getElementById('show_content');
	for (var i = choice_li.length - 1; i >= 0; i--) {
		choice_li[i].onmouseover = function(){
			this.className='menu_choice_selected display';
			//body.className='container_mv';
		};
		choice_li[i].onmouseout = function(){
			this.className='';
			//body.className='';
		};
	}
	var comment = $('#cmt .every_comment');
	for (var i = comment.length - 1; i >= 0; i--) {
		var seg = comment[i].getAttribute('thread').split('.').length;
		comment[i].style.cssText='width:'+(100-10*(seg-2))+'%;';
	};
    var reply = $('#cmt .reply');
    console.log(reply.length);
    for (var i = reply.length - 1; i >= 0; i--) {
        reply[i].onclick = function(){
            window.scrollTo(0,document.body.scrollHeight);
            var to =this.getAttribute('to');
            var thread =this.getAttribute('father');
            $('#id_thread').attr('value',thread);
            $('#cmt_title').html("你正在回复"+to);
            var concel_btn=document.getElementById('concel_cmt');
            concel_btn.style.display='block';
            concel_btn.onclick =function(){
            	$('#id_thread').attr('value','');
            	$('#cmt_title').html("期待你的评论");
            	this.style.display='none';
            }
        }
    };
}





