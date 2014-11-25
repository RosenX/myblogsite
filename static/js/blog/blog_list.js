window.onload = function(){
	//获取相关元素
	var container=getByid("container");
	var tagbox=getByid("static_box");
	//计算位置
	var top_tag=container.offsetTop+49;
	var left=container.offsetLeft+container.clientWidth*0.75;
	upTop_tag=35;
	
	window.onscroll = function(){
		var scrTop=document.body.scrollTop;
		if(scrTop+50>top_tag){
			tagbox.style.cssText="position:fixed;top:"+upTop_tag+"px;left:"+left+"px;";
		}
		else{
			tagbox.style.cssText="position:fixed;top:"+(top_tag-scrTop)+"px;left:"+left+"px;";
		}
	}

	//获取鼠标划过或点击的标签和要切换内容的元素
	var titles=getByid('static_box_header').getElementsByTagName('li');
   	var	divs=getByid('static_content').getElementsByTagName('div');
   	if (titles.length!=divs.length)return;
   	for(var i=0;i<titles.length;i++){
   		titles[i].ind=i;
   		titles[i].onmouseover = function(){
   			for(var j=0;j<titles.length;j++){
   				titles[j].className='';
   				divs[j].style.display="none";
   			}
   			this.className="select";
   			divs[this.ind].style.display="block";
   		}
   	}

   	var nav_menu =getByid('nav_menu').getElementsByTagName('a');
   	for (var i = nav_menu.length - 1; i >= 0; i--) {
   		nav_menu[i].onclick = function(){
   			this.className = 'click';
   		}
   	};

}