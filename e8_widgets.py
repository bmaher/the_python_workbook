WIDGET_WEIGHT_G = 75
GIZMO_WEIGHT_G = 112

widgets = int(input('Number of widgets: '))
gizmos = int(input('Number of gizmos: '))

total_weight = (widgets * WIDGET_WEIGHT_G) + (gizmos * GIZMO_WEIGHT_G)
print('Total weight: %sg') % total_weight
