earth_radius = float(input("Enter the radius of the Earth in kilometers: "))


def sphere_area(earth_radius):
	print("The surface area of the Earth is: ", 4 * 3.14 * earth_radius ** 2, "km²")

def sphere_volume(earth_radius):
	print("The volume of the Earth is: ", 4 / 3 * 3.14 * earth_radius ** 3, "km³")

sphere_area(earth_radius)
sphere_volume(earth_radius)
