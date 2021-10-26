function reset_search(msg=' '){
    $('li').each(function(){
        $(this).removeClass('hidden');
    });

    $('#spanSearch').text(msg);
}


$('#inpSearch').on('focusout', function(){
    $(this).val('');
    $('#spanSearch').text('');
});


$('#inpSearch').on('input', function(){
    let aux = false;
    let query = $(this).val().toString().toLowerCase();

    $('li').each(function(){
        let item = $(this).text().toLowerCase();
        if (item.indexOf(query) >= 0){
            $(this).removeClass('hidden');
            aux = true;
        }else{
            $(this).addClass('hidden');
        }
    });

    if (query=='') reset_search('')
    else if(!aux) reset_search('Não foi possivel encontrar "' + query + '"');
});


$('#modelModal').on('show.bs.modal', function (ev) {
    let tipo = ev.relatedTarget.getAttribute('data-bs-tipo');
    let id = ev.relatedTarget.getAttribute('data-bs-cand');

    if (id){
        $.ajax({
            url: 'details/',
            data: { 'id':id },
            dataType: 'json',
            success: function(data){
                $('#inpId').val(id);
                $('#inpNome').val(data.nome);
                $('#sltStatus').val(data.status);
            }
        });
    }
    
    if (tipo == 'editar'){
        $('#btnExcluir').removeClass('invisible');
    }
    else{
        $('#inpNome').val('');
        $('#sltStatus').val('0');
        $('#btnExcluir').addClass('invisible');
    }
    
    $('.modal-title').text(tipo + ' candidato');
    $('#btnSalvar').val(tipo);
});


$('#modelModal').on('shown.bs.modal', function(){
    reset_search();
});


$('#btnEspecial').on('click', function(){
    $('#ctnFirst').addClass('hidden');
    $('#ctnSecond').removeClass('hidden');
});