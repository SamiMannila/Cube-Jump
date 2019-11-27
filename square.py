class Square():
    '''
    The class Square represents a single square in a robot world.
    A square can contain either a world structure element or a player or enemy or it can be empty.
    '''

    def __init__(self, is_element=False, is_points=False, is_armament=False):
        '''
        Creates a new square. Initially there is no player or enemy in the square.

        Parameter is_wall_square is a boolean value stating whether there is a world structure element
        in the square or not: boolean
        '''

        self.is_element = is_element      # flag (one-way currently, since element can not be removed)
        self.is_points = is_points        # flag
        self.is_armament = is_armament    # flag

    def is_element_square(self):
        '''
        Returns a boolean value stating whether there is a element in the square or not: boolean
        '''
        return self.is_element

    def is_armament_square(self):
        '''
        Returns a boolean value stating whether there is a armament in the square or not: boolean
        '''
        return self.is_armament

    def is_point_square(self):
        '''
        Returns a boolean value stating whether there is a point in the square or not: boolean
        '''
        return self.is_points

    def set_element(self):
        '''
        Sets a element in this square, if possible.
        If the square was not empty, the method fails to do anything.

        Returns a boolean value indicating if the operation succeeded: boolean
        '''
        if self.is_empty():
            self.is_element = True
            return True
        else:
            return False

    def set_points(self):
        '''
        Sets points in this square, if possible.
        If the square was not empty, the method fails to do anything.

        Returns a boolean value indicating if the operation succeeded: boolean
        '''
        if self.is_empty():
            self.is_points = True
            return True
        else:
            return False

    def set_armament(self):
        '''
        Sets armament for player to collect in this square, if possible.
        If the square was not empty, the method fails to do anything.

        Returns a boolean value indicating if the operation succeeded: boolean
        '''
        if self.is_empty():
            self.is_armament = True
            return True
        else:
            return False

    def is_empty(self):
        '''
        Returns a boolean value stating whether there is a element/armament/points in the square or not: boolean
        True if empty and False if not.
        '''
        if self.is_armament or self.is_element or self.is_points:
            return False
        else:
            return True





    


