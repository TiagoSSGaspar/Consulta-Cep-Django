$(document).ready(() => {

    $("#id_cep").blur(() => {
        let formSerializeData = $("#form-cadastro-endereco").serialize();

        $.ajax({
            url: $("form-cadastro-endereco").data('url'),
            data: formSerializeData,
            type: 'post',
            success: (response) => {
                $("#id_cep").val(response.cep);
                $("#id_endereco").val(response.logradouro);
                $("#id_numero").val(response.numero);
                $("#id_complemento").val(response.complemento);
                $("#id_bairro").val(response.bairro);
                $("#id_cidade").val(response.localidade);
                $("#id_uf").val(response.uf);
                $("#id_descricao").val(response.descricao);

            }
        })

    });
});


