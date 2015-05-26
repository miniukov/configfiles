import bpy
l0 = bpy.context.user_preferences.system.solid_lights[0]
l1 = bpy.context.user_preferences.system.solid_lights[1]
l2 = bpy.context.user_preferences.system.solid_lights[2]

l0.use = True
l0.diffuse_color = (0.5436685681343079, 0.32369518280029297, 0.20761273801326752)
l0.specular_color = (0.45796120166778564, 0.45796120166778564, 0.45796120166778564)
l0.direction = (-0.07042253017425537, 0.6760563254356384, 0.733476996421814)
l1.use = True
l1.diffuse_color = (0.47794559597969055, 0.5305657386779785, 0.6605422496795654)
l1.specular_color = (0.41900360584259033, 0.41900360584259033, 0.41900360584259033)
l1.direction = (-0.09859155118465424, 0.07042253017425537, 0.9926329851150513)
l2.use = False
l2.diffuse_color = (0.2861774265766144, 0.35667064785957336, 0.3350117802619934)
l2.specular_color = (0.3956288695335388, 0.36276519298553467, 0.38725683093070984)
l2.direction = (0.881772518157959, 0.2502327561378479, -0.39982590079307556)