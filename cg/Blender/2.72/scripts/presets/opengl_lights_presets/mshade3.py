import bpy
l0 = bpy.context.user_preferences.system.solid_lights[0]
l1 = bpy.context.user_preferences.system.solid_lights[1]
l2 = bpy.context.user_preferences.system.solid_lights[2]

l0.use = True
l0.diffuse_color = (0.43621575832366943, 0.33640265464782715, 0.31929048895835876)
l0.specular_color = (0.9113942980766296, 0.8065879940986633, 0.5334088206291199)
l0.direction = (-0.012820512987673283, 0.44871795177459717, 0.8935815095901489)
l1.use = True
l1.diffuse_color = (0.5633640289306641, 0.35928845405578613, 0.24127797782421112)
l1.specular_color = (0.0, 0.0, 0.0)
l1.direction = (0.0, 0.9230769276618958, 0.38461539149284363)
l2.use = True
l2.diffuse_color = (0.36491984128952026, 0.206924706697464, 0.17659659683704376)
l2.specular_color = (0.5704712867736816, 0.5164262652397156, 0.41887882351875305)
l2.direction = (0.012177534401416779, -0.9742027521133423, -0.22534571588039398)