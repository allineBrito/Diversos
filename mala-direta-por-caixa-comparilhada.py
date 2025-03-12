import smtplib
import openpyxl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# Configurações de SMTP
smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587
smtp_username = 'email'  #conta de e-mail
smtp_password = 'senha'  #senha de e-mail
from_email = 'email.email@gmail.com'  # O endereço de e-mail da caixa compartilhada

workbook = openpyxl.load_workbook('teste_email.xlsx')
sheet = workbook.active
emails = []
nomes = []
for row in sheet.iter_rows(values_only=True):
    email = row[0]
    nome = row[1]
    if email not in emails:  # evitar duplicatas
        emails.append(email)
        nomes.append(nome)

for row in sheet.iter_rows(values_only=True):
    email = row[0]
    if email:
        emails.append(email)

subject = 'Inscrições abertas para o Conselho Nacional de Promoção da Igualdade Racial'

message = '''
<html>
    <head></head>
    <body>
        <body style="font-size: 12px;">
            <p>Olá! Tudo bem?</p>
            <p><strong>As inscri&ccedil;&otilde;es para o Conselho Nacional de Promo&ccedil;&atilde;o da Igualdade Racial (CNPIR) para o Bi&ecirc;nio 2023-2025 est&atilde;o abertas!</strong></p>

            <p>O CNPIR &eacute; um &oacute;rg&atilde;o colegiado de car&aacute;ter consultivo e integrante da estrutura regimental do Minist&eacute;rio da Igualdade Racial. Sua finalidade &eacute; propor, em &acirc;mbito nacional, pol&iacute;ticas de promo&ccedil;&atilde;o da igualdade racial, com foco na popula&ccedil;&atilde;o negra e em outros segmentos &eacute;tnicos da popula&ccedil;&atilde;o brasileira, com o objetivo de combater o racismo, o preconceito e a discrimina&ccedil;&atilde;o racial e reduzir as desigualdades raciais, inclusive nos aspectos econ&ocirc;mico, financeiro, social, pol&iacute;tico e cultural, com a amplia&ccedil;&atilde;o do processo de controle social sobre essas pol&iacute;ticas.</p>

            <p><u>As categorias de inscri&ccedil;&atilde;o dispon&iacute;veis s&atilde;o:</u></p>

            <ul>
                <li>Rede do Movimento Negro</li>
                <li>Organiza&ccedil;&atilde;o Geral do Movimento Negro</li>
                <li>Juventudes</li>
                <li>Territ&oacute;rios Perif&eacute;ricos</li>
                <li>LGBTQIA+</li>
                <li>Mulheres</li>
                <li>Trabalhadores(as)</li>
                <li>Povos e Comunidades Tradicionais de Matriz Africana</li>
                <li>Povos de Terreiros</li>
                <li>Quilombolas</li>
                <li>Povos Ciganos</li>
                <li>Enfrentamento &agrave; Xenofobia e Discrimina&ccedil;&atilde;o Racial</li>
            </ul>

            <p>As entidades interessadas em compor o CNPIR devem apresentar a candidatura por meio do preenchimento dos formul&aacute;rio,&nbsp;dispon&iacute;vel&nbsp;no site do Sistema Nacional de Direitos Humanos (SNDH). Para acessar o formul&aacute;rio de inscri&ccedil;&atilde;o, siga o link: <a href="https://sndh.mdh.gov.br/" target="_new">https://sndh.mdh.gov.br/</a>. Lembre-se de se logar como Gov.br e encontrar, no final da p&aacute;gina, a se&ccedil;&atilde;o dedicada ao Conselho Nacional de Promo&ccedil;&atilde;o da Igualdade Racial (CNPIR).&nbsp;</p>

            <p><em><strong>O prazo de inscri&ccedil;&otilde;es &eacute; de 01/09/2023 a 25/09/2023</strong></em>.</p>

            <p>Para obter informa&ccedil;&otilde;es mais detalhadas sobre o processo de inscri&ccedil;&atilde;o, sugerimos consultar o <a href="https://www.gov.br/igualdaderacial/pt-br/assuntos/copy2_of_noticias/ministerio-da-igualdade-racial-lanca-novo-edital-para-o-conselho-nacional-de-promocao-da-igualdade-racial/edital-cnpir-final-assinado.pdf">edital</a>.&nbsp;Al&eacute;m disso, para um guia passo a passo sobre como se inscrever, a plataforma do Participa+ Brasil oferece informa&ccedil;&otilde;es &uacute;teis: <a href="https://www.gov.br/participamaisbrasil/cnpir" target="_new">Participa + Brasil - Processo Seletivo CNPIR 2023-2025</a>.</p>

            <p>N&atilde;o perca a oportunidade de fazer parte deste importante conselho que trabalha incansavelmente pela promo&ccedil;&atilde;o da igualdade racial em nosso pa&iacute;s. Esperamos contar com a sua participa&ccedil;&atilde;o ativa.</p>

            <p>Para quaisquer d&uacute;vidas ou mais informa&ccedil;&otilde;es, entre em contato pelo telefone (61) 2027-3214/3294 ou pelo WhatsApp (61) 99607-0813 ou pelo email <a href="mailto:seuemaildecontato@exemplo.com" target="_new">eleicao.cnpir@igualdaderacial.gov.br</a>.</p>

            <p>&nbsp;</p>

            <p>&nbsp;</p>

            <p><cite>Atenciosamente</cite>,</p>
        </body>
        <br>
                <p style="font-size: 13px; margin: 0;">Ministério da Igualdade Racial</p>
        <p style="font-size: 13px; margin: 0;">Esplanada dos Ministérios, Bloco C, 3° andar, Sala 329</p>
                <br>
        <a href="https://ibb.co/kJvGD1p">
            <img src="https://i.ibb.co/kJvGD1p/assinatura.png" alt="Assinatura" style="width: 80px;"></a>
    </body>
</html>
'''

for to_email in emails:
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = Header(subject, 'utf-8')

    body = MIMEText(message, 'html', 'utf-8')  # Altere o tipo de conteúdo para 'html'
    msg.attach(body)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(from_email, to_email, msg.as_string())
            print(f'E-mail enviado para {to_email}')
    except Exception as e:
        print(f'Erro ao enviar e-mail para {to_email}: {str(e)}')

