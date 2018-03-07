<?php
//官网文档
//http://simplehtmldom.sourceforge.net/     下载地址：https://github.com/samacs/simple_html_dom

//学习文档
//http://blog.csdn.net/qq_30845505/article/details/51499061



include './simple_html_dom/simple_html_dom.php';
//使用url和file都可以创建DOM
$html = file_get_html('http://www.doutula.com/');


//找到所有图片
 foreach($html->find('img') as $element)
        echo $element->src . '<br>';

//找到所有链接
/*foreach($html->find('a') as $element)
       echo $element->href . '<br>';
*/







	   























