def validate_login_data(data):
    # Verifica se os campos estão presentes
    if (not isinstance(data['username'], str) or not data['username'].strip()) and (not isinstance(data['password'], str) or not data['password'].strip()):
        return False, "Os campos 'Email' e 'Senha' são obrigatórios."

    # Verifica se o username é uma string não vazia
    if not isinstance(data['username'], str) or not data['username'].strip():
        return False, "O campo 'Email' não pode estar vazio."

    # Verifica se a senha atende a um critério básico (ex: pelo menos 6 caracteres)
    if not isinstance(data['password'], str) or len(data['password']) < 6:
        return False, "O campo 'Senha' deve ter pelo menos 6 caracteres."

    # Se todas as verificações passarem, retorna True
    return True, ""