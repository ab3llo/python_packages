# Import utils submodule
# import package.utils
# Import package, because utils is imported in __init__.py 
import package

# Decide to say I love you 
package.utils.we_need_to_talk()

# Decide to break up
package.utils.we_need_to_talk(True)

# Create an instance of MyClass
my_instance = package.MyClass("Hello, World!")  

# Print output of MyClass attribute
print(my_instance.attribute)  # Output the attribute value