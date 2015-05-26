import bpy
l0 = bpy.context.user_preferences.system.solid_lights[0]
l1 = bpy.context.user_preferences.system.solid_lights[1]
l2 = bpy.context.user_preferences.system.solid_lights[2]

l0.use = True
l0.diffuse_color = (0.6399589776992798, 0.3488071858882904, 0.21334367990493774)
l0.specular_color = (0.21683719754219055, 0.21683719754219055, 0.21683719754219055)
l0.direction = (-0.028169013559818268, 0.563380241394043, 0.8257173895835876)
l1.use = True
l1.diffuse_color = (0.4103834629058838, 0.2880929708480835, 0.2370610237121582)
l1.specular_color = (0.13870155811309814, 0.19451864063739777, 0.27916958928108215)
l1.direction = (-0.43661969900131226, -0.3661971688270569, 0.8217437267303467)
l2.use = False
l2.diffuse_color = (0.47395893931388855, 0.19372320175170898, 0.144014373421669)
l2.specular_color = (0.3966449797153473, 0.41162633895874023, 0.3569863736629486)
l2.direction = (-0.2816901206970215, 0.11267605423927307, 0.9528665542602539)