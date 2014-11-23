import colander


class LoginSchema(colander.MappingSchema):
    email = colander.SchemaNode(colander.String(),
                                validator=colander.Email())
    password = colander.SchemaNode(colander.String(),
                                   validator=colander.Length(max=255))


class ArriveSchema(colander.MappingSchema):
    url = colander.SchemaNode(colander.String(),
                              validator=colander.url)
