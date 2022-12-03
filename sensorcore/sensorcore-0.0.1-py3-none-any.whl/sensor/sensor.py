

class Sensor(object):
    """Base class for sensors."""

    def __init__(self, sensor_id, sensor_type, sensor_name, sensor_unit,
                 sensor_value):
        """Initialize the sensor."""
        self._id = sensor_id
        self._type = sensor_type
        self._name = sensor_name
        self._unit = sensor_unit
        self._value = sensor_value

    @property
    def id(self):
        """Return the id of this sensor."""
        return self._id 

    @property
    def type(self):
        """Return the type of this sensor."""
        return self._type

    @property
    def name(self):
        """Return the name of this sensor."""
        return self._name
    
    @property
    def unit(self):
        """Return the unit of this sensor."""
        return self._unit
    
    @property
    def value(self):
        """Return the value of this sensor."""
        return self._value
    
    def update(self):
        """Update the sensor."""
        raise NotImplementedError()
    
    def __str__(self):
        """Return the string representation of this sensor."""
        return "%s %s %s %s" % (self._id, self._type, self._name, self._value)
    
    def __repr__(self):
        """Return the string representation of this sensor."""
        return self.__str__()
    
    def __eq__(self, other):
        """Return the comparison of this sensor with another."""
        return (self._id == other._id and
                self._type == other._type and
                self._name == other._name and
                self._unit == other._unit and
                self._value == other._value)
        
    def __ne__(self, other):
        """Return the comparison of this sensor with another."""
        return not self.__eq__(other)
    
    def __hash__(self):
        """Return a hash for this sensor."""
        return hash((self._id, self._type, self._name, self._unit, self._value))
    
    def __lt__(self, other):
        """Return the comparison of this sensor with another."""
        return self._id < other._id
    
    def __le__(self, other):
        """Return the comparison of this sensor with another."""
        return self._id <= other._id
    
    def __gt__(self, other):
        """Return the comparison of this sensor with another."""
        return self._id > other._id
    
    def __ge__(self, other):
        """Return the comparison of this sensor with another."""
        return self._id >= other._id

    