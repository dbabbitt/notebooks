
import bpy

# Get spiral data
patriarch_coords_dict = {}
patriarch_coords_dict['Thomas Bobbet'] = [(-141, -194, 1), (-140, -194, 1), (-140, -195, 1), (-139, -195, 1), (-138, -195, 1), (-138, -196, 1), (-137, -196, 1), (-137, -197, 1), (-136, -197, 1), (-136, -198, 1), (-135, -198, 1), (-135, -199, 1), (-134, -199, 1), (-133, -199, 1), (-133, -200, 1), (-132, -200, 1), (-132, -201, 1), (-131, -201, 1), (-131, -202, 1), (-130, -202, 1), (-129, -202, 1), (-129, -203, 1), (-128, -203, 1), (-128, -204, 1), (-127, -204, 1), (-127, -205, 1), (-126, -205, 1), (-125, -205, 1), (-125, -206, 1), (-124, -206, 1), (-124, -207, 1), (-123, -207, 1), (-122, -207, 1), (-122, -208, 1), (-121, -208, 1), (-121, -209, 1), (-120, -209, 1), (-119, -209, 1), (-119, -210, 1), (-118, -210, 1), (-118, -211, 1), (-117, -211, 1), (-116, -211, 1), (-116, -212, 1), (-115, -212, 1), (-115, -213, 1), (-114, -213, 1), (-113, -213, 1), (-113, -214, 1), (-112, -214, 1), (-111, -214, 1), (-111, -215, 1), (-110, -215, 1), (-110, -216, 1), (-109, -216, 1), (-108, -216, 1), (-108, -217, 1), (-107, -217, 1), (-106, -217, 1), (-106, -218, 1), (-105, -218, 1), (-105, -219, 1), (-104, -219, 1), (-103, -219, 1), (-103, -220, 1), (-102, -220, 1), (-101, -220, 1), (-101, -221, 1), (-100, -221, 1), (-99, -221, 1), (-99, -222, 1), (-98, -222, 1), (-97, -222, 1), (-97, -223, 1), (-96, -223, 1), (-95, -223, 1), (-95, -224, 1), (-94, -224, 1), (-93, -224, 1), (-93, -225, 1), (-92, -225, 1), (-91, -225, 1), (-91, -226, 1), (-90, -226, 1), (-89, -226, 1), (-89, -227, 1), (-88, -227, 1), (-87, -227, 1), (-87, -228, 1), (-86, -228, 1), (-85, -228, 1), (-85, -229, 1), (-84, -229, 1), (-83, -229, 1), (-82, -229, 1), (-82, -230, 1), (-81, -230, 1), (-80, -230, 1), (-80, -231, 1), (-79, -231, 1), (-78, -231, 1), (-78, -232, 1), (-77, -232, 1), (-76, -232, 1), (-75, -232, 1), (-75, -233, 1), (-74, -233, 1), (-73, -233, 1), (-73, -234, 1), (-72, -234, 1), (-71, -234, 1), (-70, -234, 1), (-70, -235, 1), (-69, -235, 1), (-68, -235, 1), (-67, -235, 1), (-67, -236, 1), (-66, -236, 1), (-65, -236, 1), (-64, -236, 1), (-64, -237, 1), (-63, -237, 1), (-62, -237, 1), (-61, -238, 1), (-60, -238, 1), (-59, -238, 1), (-58, -238, 1), (-58, -239, 1), (-57, -239, 1), (-56, -239, 1), (-55, -239, 1), (-55, -240, 1), (-54, -240, 1), (-53, -240, 1), (-52, -240, 1), (-52, -241, 1), (-51, -241, 1), (-50, -241, 1), (-49, -241, 1), (-48, -241, 1), (-48, -242, 1), (-47, -242, 1), (-46, -242, 1), (-45, -242, 1), (-44, -242, 1), (-44, -243, 1), (-43, -243, 1), (-42, -243, 1), (-41, -243, 1), (-40, -243, 1), (-40, -244, 1), (-39, -244, 1), (-38, -244, 1), (-37, -244, 1), (-36, -244, 1), (-36, -245, 1), (-35, -245, 1), (-34, -245, 1), (-33, -245, 1), (-32, -245, 1), (-31, -245, 1), (-31, -246, 1), (-30, -246, 1), (-29, -246, 1), (-28, -246, 1), (-27, -246, 1), (-26, -246, 1), (-25, -246, 1), (-25, -247, 1), (-24, -247, 1), (-23, -247, 1), (-22, -247, 1), (-21, -247, 1), (-20, -247, 1), (-19, -247, 1), (-19, -248, 1), (-18, -248, 1), (-17, -248, 1), (-16, -248, 1), (-15, -248, 1)]
patriarch_coords_dict['(No Name), Jr.'] = [(-81, 162, 1), (-82, 162, 1), (-83, 162, 1), (-84, 162, 1), (-84, 161, 1), (-85, 161, 1), (-86, 161, 1), (-86, 160, 1), (-87, 160, 1), (-88, 160, 1), (-89, 159, 1), (-90, 159, 1), (-91, 159, 1), (-91, 158, 1), (-92, 158, 1), (-93, 158, 1), (-93, 157, 1), (-94, 157, 1), (-95, 157, 1), (-95, 156, 1), (-96, 156, 1), (-97, 156, 1), (-97, 155, 1), (-98, 155, 1), (-99, 155, 1), (-99, 154, 1), (-100, 154, 1), (-101, 153, 1), (-102, 153, 1), (-103, 152, 1), (-104, 152, 1), (-105, 151, 1), (-106, 151, 1), (-106, 150, 1), (-107, 150, 1), (-108, 149, 1), (-109, 149, 1), (-110, 148, 1), (-111, 148, 1), (-111, 147, 1), (-112, 147, 1), (-113, 146, 1), (-114, 146, 1), (-114, 145, 1), (-115, 145, 1), (-116, 144, 1), (-117, 144, 1), (-117, 143, 1), (-118, 143, 1), (-119, 143, 1), (-119, 142, 1), (-120, 142, 1), (-120, 141, 1), (-121, 141, 1), (-122, 140, 1), (-123, 140, 1), (-123, 139, 1), (-124, 139, 1), (-124, 138, 1), (-125, 138, 1), (-125, 137, 1), (-126, 137, 1), (-127, 136, 1), (-128, 136, 1), (-128, 135, 1), (-129, 135, 1), (-129, 134, 1), (-130, 134, 1), (-130, 133, 1), (-131, 133, 1), (-132, 132, 1), (-133, 132, 1), (-133, 131, 1), (-134, 131, 1), (-134, 130, 1), (-135, 130, 1), (-135, 129, 1), (-136, 129, 1), (-136, 128, 1), (-137, 128, 1), (-138, 127, 1), (-139, 126, 1), (-140, 125, 1), (-141, 124, 1), (-142, 123, 1), (-143, 123, 1), (-143, 122, 1), (-144, 122, 1), (-144, 121, 1), (-145, 120, 1), (-146, 119, 1), (-147, 119, 1), (-147, 118, 1), (-148, 117, 1), (-149, 116, 1), (-150, 115, 1), (-150, 114, 1), (-151, 114, 1), (-151, 113, 1), (-152, 113, 1), (-152, 112, 1), (-153, 112, 1), (-153, 111, 1), (-154, 111, 1), (-154, 110, 1), (-155, 109, 1), (-156, 108, 1), (-156, 107, 1), (-157, 107, 1), (-157, 106, 1), (-158, 106, 1), (-158, 105, 1), (-159, 105, 1), (-159, 104, 1), (-160, 103, 1), (-160, 102, 1), (-161, 102, 1), (-161, 101, 1), (-162, 101, 1), (-162, 100, 1), (-163, 99, 1), (-163, 98, 1), (-164, 98, 1), (-164, 97, 1), (-165, 97, 1), (-165, 96, 1), (-166, 95, 1), (-166, 94, 1), (-167, 94, 1), (-167, 93, 1), (-168, 92, 1), (-168, 91, 1), (-169, 91, 1), (-169, 90, 1), (-169, 89, 1), (-170, 89, 1), (-170, 88, 1), (-171, 87, 1), (-171, 86, 1), (-172, 86, 1), (-172, 85, 1), (-172, 84, 1), (-173, 84, 1), (-173, 83, 1), (-174, 83, 1), (-174, 82, 1), (-174, 81, 1), (-175, 81, 1), (-175, 80, 1), (-176, 79, 1), (-176, 78, 1), (-177, 77, 1), (-177, 76, 1), (-178, 75, 1), (-178, 74, 1), (-179, 74, 1), (-179, 73, 1), (-179, 72, 1), (-180, 72, 1), (-180, 71, 1), (-180, 70, 1), (-181, 69, 1), (-181, 68, 1), (-182, 67, 1), (-182, 66, 1), (-183, 65, 1), (-183, 64, 1), (-183, 63, 1), (-184, 63, 1), (-184, 62, 1), (-184, 61, 1), (-185, 61, 1), (-185, 60, 1), (-185, 59, 1), (-186, 58, 1), (-186, 57, 1), (-186, 56, 1), (-187, 56, 1), (-187, 55, 1), (-187, 54, 1), (-188, 53, 1), (-188, 52, 1), (-188, 51, 1), (-189, 50, 1), (-189, 49, 1), (-189, 48, 1), (-190, 48, 1), (-190, 47, 1), (-190, 46, 1), (-190, 45, 1), (-191, 44, 1), (-191, 43, 1), (-191, 42, 1), (-192, 41, 1), (-192, 40, 1), (-192, 39, 1), (-192, 38, 1), (-193, 38, 1), (-193, 37, 1), (-193, 36, 1), (-193, 35, 1), (-194, 34, 1), (-194, 33, 1), (-194, 32, 1), (-194, 31, 1), (-195, 30, 1), (-195, 29, 1), (-195, 28, 1), (-195, 27, 1), (-196, 26, 1), (-196, 25, 1), (-196, 24, 1), (-196, 23, 1), (-196, 22, 1), (-197, 21, 1), (-197, 20, 1), (-197, 19, 1), (-197, 18, 1), (-197, 17, 1), (-197, 16, 1), (-198, 16, 1), (-198, 15, 1), (-198, 14, 1), (-198, 13, 1), (-198, 12, 1), (-198, 11, 1), (-198, 10, 1), (-198, 9, 1), (-199, 9, 1), (-199, 8, 1), (-199, 7, 1), (-199, 6, 1), (-199, 5, 1), (-199, 4, 1), (-199, 3, 1), (-199, 2, 1), (-199, 1, 1), (-199, 0, 1), (-200, 0, 1), (-200, -1, 1), (-200, -2, 1), (-200, -3, 1), (-200, -4, 1), (-200, -5, 1), (-200, -6, 1), (-200, -7, 1), (-200, -8, 1), (-200, -9, 1), (-200, -10, 1), (-200, -11, 1), (-200, -12, 1), (-200, -13, 1), (-200, -14, 1), (-200, -15, 1), (-200, -16, 1), (-200, -17, 1), (-200, -18, 1), (-200, -19, 1), (-200, -20, 1), (-200, -21, 1), (-200, -22, 1), (-200, -23, 1), (-200, -24, 1), (-200, -25, 1), (-200, -26, 1), (-200, -27, 1), (-200, -28, 1), (-200, -29, 1), (-200, -30, 1), (-200, -31, 1), (-199, -31, 1), (-199, -32, 1), (-199, -33, 1), (-199, -34, 1), (-199, -35, 1), (-199, -36, 1), (-199, -37, 1), (-199, -38, 1), (-199, -39, 1), (-199, -40, 1), (-199, -41, 1), (-198, -41, 1), (-198, -42, 1), (-198, -43, 1), (-198, -44, 1), (-198, -45, 1), (-198, -46, 1), (-198, -47, 1), (-197, -48, 1), (-197, -49, 1), (-197, -50, 1), (-197, -51, 1), (-197, -52, 1), (-197, -53, 1), (-196, -54, 1), (-196, -55, 1), (-196, -56, 1), (-196, -57, 1), (-196, -58, 1), (-195, -58, 1), (-195, -59, 1), (-195, -60, 1), (-195, -61, 1), (-195, -62, 1), (-195, -63, 1), (-194, -63, 1), (-194, -64, 1), (-194, -65, 1), (-194, -66, 1), (-194, -67, 1), (-193, -67, 1), (-193, -68, 1), (-193, -69, 1), (-193, -70, 1), (-192, -71, 1), (-192, -72, 1), (-192, -73, 1), (-191, -74, 1), (-191, -75, 1), (-191, -76, 1), (-191, -77, 1), (-190, -77, 1), (-190, -78, 1), (-190, -79, 1), (-190, -80, 1), (-189, -80, 1), (-189, -81, 1), (-189, -82, 1), (-189, -83, 1), (-188, -83, 1), (-188, -84, 1), (-188, -85, 1), (-188, -86, 1), (-187, -86, 1), (-187, -87, 1), (-187, -88, 1), (-186, -89, 1), (-186, -90, 1), (-186, -91, 1), (-185, -91, 1), (-185, -92, 1), (-185, -93, 1), (-184, -94, 1), (-184, -95, 1), (-184, -96, 1), (-183, -96, 1), (-183, -97, 1), (-183, -98, 1), (-182, -98, 1), (-182, -99, 1), (-182, -100, 1), (-181, -101, 1), (-181, -102, 1), (-180, -103, 1), (-180, -104, 1), (-179, -105, 1), (-179, -106, 1), (-179, -107, 1), (-178, -107, 1), (-178, -108, 1), (-177, -109, 1), (-177, -110, 1), (-176, -111, 1), (-176, -112, 1), (-175, -112, 1), (-175, -113, 1), (-175, -114, 1), (-174, -115, 1), (-174, -116, 1), (-173, -116, 1), (-173, -117, 1), (-173, -118, 1), (-172, -118, 1), (-172, -119, 1), (-171, -120, 1), (-171, -121, 1), (-170, -121, 1), (-170, -122, 1), (-169, -123, 1), (-169, -124, 1), (-168, -124, 1), (-168, -125, 1), (-168, -126, 1), (-167, -126, 1), (-167, -127, 1), (-166, -128, 1), (-166, -129, 1), (-165, -129, 1), (-165, -130, 1), (-164, -131, 1), (-164, -132, 1), (-163, -132, 1), (-163, -133, 1), (-162, -134, 1), (-162, -135, 1), (-161, -135, 1), (-161, -136, 1), (-160, -136, 1), (-160, -137, 1), (-159, -138, 1), (-159, -139, 1), (-158, -139, 1), (-158, -140, 1), (-157, -140, 1), (-157, -141, 1), (-157, -142, 1), (-156, -142, 1), (-156, -143, 1), (-155, -143, 1), (-155, -144, 1), (-154, -144, 1), (-154, -145, 1), (-153, -145, 1), (-153, -146, 1), (-152, -147, 1), (-152, -148, 1), (-151, -148, 1), (-151, -149, 1), (-150, -149, 1), (-150, -150, 1), (-149, -150, 1), (-149, -151, 1), (-148, -151, 1), (-148, -152, 1), (-147, -153, 1), (-146, -154, 1), (-146, -155, 1), (-145, -155, 1), (-145, -156, 1), (-144, -156, 1), (-144, -157, 1), (-143, -157, 1), (-143, -158, 1), (-142, -158, 1), (-142, -159, 1), (-141, -159, 1), (-141, -160, 1), (-140, -160, 1), (-140, -161, 1), (-139, -161, 1), (-139, -162, 1), (-138, -162, 1), (-138, -163, 1), (-137, -163, 1), (-137, -164, 1), (-136, -164, 1), (-136, -165, 1), (-135, -165, 1), (-135, -166, 1), (-134, -166, 1), (-134, -167, 1), (-133, -167, 1), (-132, -168, 1), (-131, -169, 1), (-130, -170, 1), (-129, -171, 1), (-128, -171, 1), (-128, -172, 1), (-127, -172, 1), (-127, -173, 1), (-126, -173, 1), (-126, -174, 1), (-125, -174, 1), (-124, -175, 1), (-123, -176, 1), (-122, -176, 1), (-122, -177, 1), (-121, -177, 1), (-121, -178, 1), (-120, -178, 1), (-119, -179, 1), (-118, -179, 1), (-118, -180, 1), (-117, -180, 1), (-117, -181, 1), (-116, -181, 1), (-115, -182, 1), (-114, -183, 1), (-113, -183, 1), (-113, -184, 1), (-112, -184, 1), (-111, -185, 1), (-110, -186, 1), (-109, -186, 1), (-108, -187, 1), (-107, -188, 1), (-106, -188, 1), (-106, -189, 1), (-105, -189, 1), (-104, -189, 1), (-104, -190, 1), (-103, -190, 1), (-103, -191, 1), (-102, -191, 1), (-101, -191, 1), (-101, -192, 1), (-100, -192, 1), (-99, -193, 1), (-98, -193, 1), (-98, -194, 1), (-97, -194, 1), (-96, -194, 1), (-96, -195, 1), (-95, -195, 1), (-94, -196, 1), (-93, -196, 1), (-92, -197, 1), (-91, -197, 1), (-91, -198, 1), (-90, -198, 1), (-89, -198, 1), (-89, -199, 1), (-88, -199, 1), (-87, -200, 1), (-86, -200, 1), (-85, -200, 1), (-85, -201, 1), (-84, -201, 1), (-83, -202, 1), (-82, -202, 1), (-81, -203, 1), (-80, -203, 1), (-79, -204, 1), (-78, -204, 1), (-77, -204, 1), (-77, -205, 1), (-76, -205, 1), (-75, -205, 1), (-75, -206, 1), (-74, -206, 1), (-73, -206, 1), (-73, -207, 1), (-72, -207, 1), (-71, -207, 1), (-70, -208, 1), (-69, -208, 1), (-68, -208, 1), (-68, -209, 1), (-67, -209, 1), (-66, -209, 1), (-65, -210, 1), (-64, -210, 1), (-63, -210, 1), (-63, -211, 1), (-62, -211, 1), (-61, -211, 1), (-60, -212, 1), (-59, -212, 1), (-58, -212, 1), (-57, -213, 1), (-56, -213, 1), (-55, -213, 1), (-54, -214, 1), (-53, -214, 1), (-52, -214, 1), (-52, -215, 1), (-51, -215, 1), (-50, -215, 1), (-49, -215, 1), (-48, -216, 1), (-47, -216, 1), (-46, -216, 1), (-45, -216, 1), (-45, -217, 1), (-44, -217, 1), (-43, -217, 1), (-42, -217, 1), (-41, -218, 1), (-40, -218, 1), (-39, -218, 1), (-38, -218, 1), (-37, -219, 1), (-36, -219, 1), (-35, -219, 1), (-34, -219, 1), (-33, -219, 1), (-33, -220, 1), (-32, -220, 1), (-31, -220, 1), (-30, -220, 1), (-29, -220, 1), (-28, -221, 1), (-27, -221, 1), (-26, -221, 1), (-25, -221, 1), (-24, -221, 1), (-23, -222, 1), (-22, -222, 1), (-21, -222, 1), (-20, -222, 1), (-19, -222, 1), (-18, -222, 1), (-17, -223, 1), (-16, -223, 1), (-15, -223, 1), (-14, -223, 1), (-13, -223, 1)]
patriarch_coords_dict['(No Name), Sr.'] = [(125, 8, 1), (125, 9, 1), (125, 10, 1), (125, 11, 1), (125, 12, 1), (125, 13, 1), (125, 14, 1), (125, 15, 1), (125, 16, 1), (125, 17, 1), (125, 18, 1), (125, 19, 1), (125, 20, 1), (125, 21, 1), (125, 22, 1), (125, 23, 1), (125, 24, 1), (125, 25, 1), (125, 26, 1), (125, 27, 1), (125, 28, 1), (125, 29, 1), (125, 30, 1), (125, 31, 1), (124, 31, 1), (124, 32, 1), (124, 33, 1), (124, 34, 1), (124, 35, 1), (124, 36, 1), (124, 37, 1), (123, 38, 1), (123, 39, 1), (123, 40, 1), (123, 41, 1), (123, 42, 1), (123, 43, 1), (122, 43, 1), (122, 44, 1), (122, 45, 1), (122, 46, 1), (122, 47, 1), (121, 47, 1), (121, 48, 1), (121, 49, 1), (121, 50, 1), (120, 51, 1), (120, 52, 1), (120, 53, 1), (120, 54, 1), (119, 55, 1), (119, 56, 1), (119, 57, 1), (118, 57, 1), (118, 58, 1), (118, 59, 1), (118, 60, 1), (117, 60, 1), (117, 61, 1), (117, 62, 1), (116, 63, 1), (116, 64, 1), (115, 65, 1), (115, 66, 1), (115, 67, 1), (114, 68, 1), (114, 69, 1), (113, 70, 1), (113, 71, 1), (112, 72, 1), (112, 73, 1), (111, 74, 1), (111, 75, 1), (110, 76, 1), (110, 77, 1), (109, 78, 1), (109, 79, 1), (108, 79, 1), (108, 80, 1), (108, 81, 1), (107, 81, 1), (107, 82, 1), (106, 83, 1), (106, 84, 1), (105, 85, 1), (104, 86, 1), (104, 87, 1), (103, 88, 1), (102, 89, 1), (102, 90, 1), (101, 91, 1), (100, 92, 1), (100, 93, 1), (99, 94, 1), (98, 95, 1), (97, 96, 1), (97, 97, 1), (96, 98, 1), (95, 99, 1), (94, 100, 1), (93, 101, 1), (92, 102, 1), (91, 103, 1), (91, 104, 1), (90, 104, 1), (90, 105, 1), (89, 105, 1), (89, 106, 1), (88, 106, 1), (88, 107, 1), (87, 107, 1), (87, 108, 1), (86, 108, 1), (86, 109, 1), (85, 109, 1), (85, 110, 1), (84, 110, 1), (84, 111, 1), (83, 111, 1), (83, 112, 1), (82, 112, 1), (82, 113, 1), (81, 113, 1), (81, 114, 1), (80, 114, 1), (80, 115, 1), (79, 115, 1), (78, 116, 1), (77, 117, 1), (76, 118, 1), (75, 119, 1), (74, 119, 1), (73, 120, 1), (72, 121, 1), (71, 122, 1), (70, 122, 1), (70, 123, 1), (69, 123, 1), (68, 124, 1), (67, 124, 1), (67, 125, 1), (66, 125, 1), (66, 126, 1), (65, 126, 1), (64, 126, 1), (64, 127, 1), (63, 127, 1), (63, 128, 1), (62, 128, 1), (61, 128, 1), (61, 129, 1), (60, 129, 1), (59, 130, 1), (58, 130, 1), (57, 131, 1), (56, 131, 1), (56, 132, 1), (55, 132, 1), (54, 132, 1), (54, 133, 1), (53, 133, 1), (52, 134, 1), (51, 134, 1), (50, 135, 1), (49, 135, 1), (48, 136, 1), (47, 136, 1), (46, 137, 1), (45, 137, 1), (44, 137, 1), (43, 138, 1), (42, 138, 1), (41, 139, 1), (40, 139, 1), (39, 140, 1), (38, 140, 1), (37, 140, 1), (36, 141, 1), (35, 141, 1), (34, 141, 1), (34, 142, 1), (33, 142, 1), (32, 142, 1), (31, 142, 1), (31, 143, 1), (30, 143, 1), (29, 143, 1), (28, 144, 1), (27, 144, 1), (26, 144, 1), (25, 145, 1), (24, 145, 1), (23, 145, 1), (22, 145, 1), (21, 146, 1), (20, 146, 1), (19, 146, 1), (18, 146, 1), (17, 146, 1), (17, 147, 1), (16, 147, 1), (15, 147, 1), (14, 147, 1), (13, 147, 1), (12, 148, 1), (11, 148, 1), (10, 148, 1), (9, 148, 1), (8, 148, 1), (7, 149, 1), (6, 149, 1), (5, 149, 1), (4, 149, 1), (3, 149, 1), (2, 149, 1), (1, 149, 1), (0, 149, 1), (0, 150, 1), (-1, 150, 1), (-2, 150, 1), (-3, 150, 1), (-4, 150, 1), (-5, 150, 1), (-6, 150, 1), (-7, 150, 1), (-8, 150, 1), (-9, 150, 1), (-10, 150, 1), (-11, 150, 1), (-12, 150, 1), (-13, 150, 1), (-14, 150, 1), (-15, 150, 1), (-16, 150, 1), (-17, 150, 1), (-18, 150, 1), (-19, 150, 1), (-20, 150, 1), (-21, 150, 1), (-22, 150, 1), (-23, 150, 1), (-24, 150, 1), (-25, 150, 1), (-26, 150, 1), (-27, 150, 1), (-28, 150, 1), (-29, 150, 1), (-30, 150, 1), (-31, 150, 1), (-31, 149, 1), (-32, 149, 1), (-33, 149, 1), (-34, 149, 1), (-35, 149, 1), (-36, 149, 1), (-37, 149, 1), (-38, 149, 1), (-39, 148, 1), (-40, 148, 1), (-41, 148, 1), (-42, 148, 1), (-43, 148, 1), (-44, 148, 1), (-45, 147, 1), (-46, 147, 1), (-47, 147, 1), (-48, 147, 1), (-49, 147, 1), (-50, 146, 1), (-51, 146, 1), (-52, 146, 1), (-53, 146, 1), (-53, 145, 1), (-54, 145, 1), (-55, 145, 1), (-56, 145, 1), (-57, 145, 1), (-57, 144, 1), (-58, 144, 1), (-59, 144, 1), (-60, 144, 1), (-60, 143, 1), (-61, 143, 1), (-62, 143, 1), (-63, 143, 1), (-64, 143, 1), (-64, 142, 1), (-65, 142, 1), (-66, 142, 1), (-67, 141, 1), (-68, 141, 1), (-69, 141, 1), (-70, 140, 1), (-71, 140, 1), (-72, 139, 1), (-73, 139, 1), (-74, 139, 1), (-75, 138, 1), (-76, 138, 1), (-77, 138, 1), (-77, 137, 1), (-78, 137, 1), (-79, 137, 1), (-80, 136, 1), (-81, 136, 1), (-82, 135, 1), (-83, 135, 1), (-83, 134, 1), (-84, 134, 1), (-85, 134, 1), (-85, 133, 1), (-86, 133, 1), (-87, 133, 1), (-88, 132, 1), (-89, 131, 1), (-90, 131, 1), (-91, 131, 1), (-91, 130, 1), (-92, 130, 1), (-93, 129, 1), (-94, 129, 1), (-95, 128, 1), (-96, 128, 1), (-96, 127, 1), (-97, 127, 1), (-98, 126, 1), (-99, 125, 1), (-100, 125, 1), (-101, 125, 1), (-101, 124, 1), (-102, 124, 1), (-103, 123, 1), (-104, 122, 1), (-105, 122, 1), (-105, 121, 1), (-106, 121, 1), (-107, 120, 1), (-108, 119, 1), (-109, 119, 1), (-109, 118, 1), (-110, 118, 1), (-111, 117, 1), (-112, 116, 1), (-113, 116, 1), (-113, 115, 1), (-114, 115, 1), (-115, 114, 1), (-116, 113, 1), (-117, 112, 1), (-118, 111, 1), (-119, 111, 1), (-119, 110, 1), (-120, 110, 1), (-121, 109, 1), (-122, 108, 1), (-122, 107, 1), (-123, 107, 1), (-124, 106, 1), (-125, 105, 1), (-125, 104, 1), (-126, 104, 1), (-127, 103, 1), (-128, 102, 1), (-128, 101, 1), (-129, 101, 1), (-130, 100, 1), (-131, 99, 1), (-131, 98, 1), (-132, 98, 1), (-133, 97, 1), (-133, 96, 1), (-134, 96, 1), (-134, 95, 1), (-135, 94, 1), (-136, 93, 1), (-136, 92, 1), (-137, 92, 1), (-138, 91, 1), (-138, 90, 1), (-139, 90, 1), (-139, 89, 1), (-140, 88, 1), (-141, 87, 1), (-141, 86, 1), (-142, 86, 1), (-142, 85, 1), (-143, 84, 1), (-144, 83, 1), (-144, 82, 1), (-145, 81, 1), (-146, 80, 1), (-146, 79, 1), (-147, 79, 1), (-147, 78, 1), (-148, 77, 1), (-148, 76, 1), (-149, 76, 1), (-149, 75, 1), (-150, 74, 1), (-150, 73, 1), (-151, 72, 1), (-151, 71, 1), (-152, 71, 1), (-152, 70, 1), (-153, 69, 1), (-153, 68, 1), (-154, 67, 1), (-154, 66, 1), (-155, 65, 1), (-155, 64, 1), (-156, 64, 1), (-156, 63, 1), (-156, 62, 1), (-157, 61, 1), (-158, 60, 1), (-158, 59, 1), (-158, 58, 1), (-159, 57, 1), (-160, 56, 1), (-160, 55, 1), (-160, 54, 1), (-161, 53, 1), (-161, 52, 1), (-162, 51, 1), (-162, 50, 1), (-162, 49, 1), (-163, 48, 1), (-163, 47, 1), (-164, 46, 1), (-164, 45, 1), (-164, 44, 1), (-165, 44, 1), (-165, 43, 1), (-165, 42, 1), (-165, 41, 1), (-166, 40, 1), (-166, 39, 1), (-166, 38, 1), (-167, 38, 1), (-167, 37, 1), (-167, 36, 1), (-167, 35, 1), (-168, 34, 1), (-168, 33, 1), (-168, 32, 1), (-169, 31, 1), (-169, 30, 1), (-169, 29, 1), (-169, 28, 1), (-170, 27, 1), (-170, 26, 1), (-170, 25, 1), (-171, 24, 1), (-171, 23, 1), (-171, 22, 1), (-171, 21, 1), (-171, 20, 1), (-172, 19, 1), (-172, 18, 1), (-172, 17, 1), (-172, 16, 1), (-172, 15, 1), (-173, 14, 1), (-173, 13, 1), (-173, 12, 1), (-173, 11, 1), (-173, 10, 1), (-173, 9, 1), (-174, 8, 1), (-174, 7, 1), (-174, 6, 1), (-174, 5, 1), (-174, 4, 1), (-174, 3, 1), (-174, 2, 1), (-174, 1, 1), (-174, 0, 1), (-175, 0, 1), (-175, -1, 1), (-175, -2, 1), (-175, -3, 1), (-175, -4, 1), (-175, -5, 1), (-175, -6, 1), (-175, -7, 1), (-175, -8, 1), (-175, -9, 1), (-175, -10, 1), (-175, -11, 1), (-175, -12, 1), (-175, -13, 1), (-175, -14, 1), (-175, -15, 1), (-175, -16, 1), (-175, -17, 1), (-175, -18, 1), (-175, -19, 1), (-175, -20, 1), (-175, -21, 1), (-175, -22, 1), (-175, -23, 1), (-175, -24, 1), (-175, -25, 1), (-175, -26, 1), (-175, -27, 1), (-175, -28, 1), (-175, -29, 1), (-175, -30, 1), (-175, -31, 1), (-174, -32, 1), (-174, -33, 1), (-174, -34, 1), (-174, -35, 1), (-174, -36, 1), (-174, -37, 1), (-174, -38, 1), (-174, -39, 1), (-173, -40, 1), (-173, -41, 1), (-173, -42, 1), (-173, -43, 1), (-173, -44, 1), (-173, -45, 1), (-173, -46, 1), (-172, -47, 1), (-172, -48, 1), (-172, -49, 1), (-172, -50, 1), (-172, -51, 1), (-171, -52, 1), (-171, -53, 1), (-171, -54, 1), (-171, -55, 1), (-171, -56, 1), (-170, -57, 1), (-170, -58, 1), (-170, -59, 1), (-169, -60, 1), (-169, -61, 1), (-169, -62, 1), (-169, -63, 1), (-168, -64, 1), (-168, -65, 1), (-168, -66, 1), (-168, -67, 1), (-167, -68, 1), (-167, -69, 1), (-166, -70, 1), (-166, -71, 1), (-166, -72, 1), (-166, -73, 1), (-165, -74, 1), (-165, -75, 1), (-165, -76, 1), (-164, -77, 1), (-164, -78, 1), (-163, -79, 1), (-163, -80, 1), (-163, -81, 1), (-162, -82, 1), (-162, -83, 1), (-162, -84, 1), (-161, -84, 1), (-161, -85, 1), (-160, -86, 1), (-160, -87, 1), (-160, -88, 1), (-159, -89, 1), (-159, -90, 1), (-159, -91, 1), (-158, -91, 1), (-158, -92, 1), (-157, -93, 1), (-157, -94, 1), (-157, -95, 1), (-156, -96, 1), (-156, -97, 1), (-155, -97, 1), (-155, -98, 1), (-154, -99, 1), (-154, -100, 1), (-153, -101, 1), (-153, -102, 1), (-152, -103, 1), (-152, -104, 1), (-151, -105, 1), (-151, -106, 1), (-150, -107, 1), (-149, -108, 1), (-149, -109, 1), (-148, -110, 1), (-148, -111, 1), (-147, -112, 1), (-146, -113, 1), (-146, -114, 1), (-145, -115, 1), (-145, -116, 1), (-144, -116, 1), (-143, -117, 1), (-143, -118, 1), (-142, -119, 1), (-142, -120, 1), (-141, -120, 1), (-141, -121, 1), (-140, -122, 1), (-140, -123, 1), (-139, -123, 1), (-138, -124, 1), (-138, -125, 1), (-137, -126, 1), (-137, -127, 1), (-136, -127, 1), (-135, -128, 1), (-135, -129, 1), (-134, -130, 1), (-133, -131, 1), (-132, -132, 1), (-132, -133, 1), (-131, -133, 1), (-130, -134, 1), (-130, -135, 1), (-129, -135, 1), (-128, -136, 1), (-128, -137, 1), (-127, -138, 1), (-126, -139, 1), (-125, -140, 1), (-125, -141, 1), (-124, -141, 1), (-123, -142, 1), (-122, -143, 1), (-121, -144, 1), (-120, -145, 1), (-119, -146, 1), (-118, -147, 1), (-117, -148, 1), (-116, -149, 1), (-115, -149, 1), (-115, -150, 1), (-114, -151, 1), (-113, -151, 1), (-112, -152, 1), (-112, -153, 1), (-111, -153, 1), (-110, -154, 1), (-110, -155, 1), (-109, -155, 1), (-108, -156, 1), (-107, -157, 1), (-106, -157, 1), (-106, -158, 1), (-105, -158, 1), (-104, -159, 1), (-103, -160, 1), (-102, -161, 1)]


for patriarch_name, coords in patriarch_coords_dict.items():
    
    # create the Curve Datablock
    curveData = bpy.data.curves.new(patriarch_name, type='CURVE')
    curveData.dimensions = '3D'
    curveData.resolution_u = 2
    
    # map coords to spline
    polyline = curveData.splines.new('NURBS')
    polyline.points.add(len(coords))
    for i, coord in enumerate(coords):
        x,y,z = coord
        polyline.points[i].co = (x, y, z, 1)

    # create Object
    curveOB = bpy.data.objects.new(patriarch_name, curveData)

    # attach to scene and validate context
    scn = bpy.context.scene
    scn.objects.link(curveOB)
    scn.objects.active = curveOB
    curveOB.select = True