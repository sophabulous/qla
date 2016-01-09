

	(function ($){
		$(document).ready(function (){
			
			$modal = $('#myModal');
		
			$('.gallery img').click(function (e){
				
				$img = $(e.target);
				$modal.find('.modal-title').html($img.attr('alt'));
				$modal.find('.modal-body .thumbnail img').attr('src', $img.attr('src'));
				
				$modal.modal('show');
			})
		})
	})(jQuery);
