# Mouse Controller Architecture

## Overview
Mouse Controller is designed as a modular Python application with clear separation between core logic, user interfaces, and utility functions.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interfaces                         │
├─────────────────────────┬───────────────────────────────────┤
│     Console Interface   │         GUI Interface             │
│     (main.py)          │      (gui/interface.py)          │
└─────────────────────────┴───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    Core Logic                              │
├─────────────────────────┬───────────────────────────────────┤
│     MouseMover          │      PatternGenerator             │
│  (core/mouse_mover.py)  │    (core/patterns.py)            │
│                        │                                   │
│ • Position control      │ • Geometric shapes                │
│ • Movement validation   │ • Complex patterns                │
│ • Safety mechanisms     │ • Random movements                │
│ • Error handling        │ • Custom patterns                 │
└─────────────────────────┴───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  Utility Layer                             │
├─────────────────────────────────────────────────────────────┤
│                 helpers.py                                 │
│                                                            │
│ • Coordinate validation    • Screen utilities              │
│ • Mathematical functions   • Safety checks                 │
│ • Interpolation           • Random generators              │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                 External Dependencies                      │
├─────────────────────────────────────────────────────────────┤
│  PyAutoGUI              │  Tkinter       │  Standard Lib    │
│  • Mouse control        │  • GUI widgets │  • Math, logging │
│  • Screen detection     │  • Threading   │  • Time, random  │
└─────────────────────────────────────────────────────────────┘
```

## Component Details

### MouseMover (Core)
**Responsibility**: Primary interface for mouse cursor control
- **Methods**: 
  - `move_to_position()`: Absolute positioning
  - `move_relative()`: Relative movement
  - `move_in_circle()`, `move_in_square()`: Basic shapes
  - `move_smooth_path()`: Path following
  - `shake_cursor()`: Random movement
  - `emergency_stop()`: Safety mechanism

**Design Patterns**:
- **Strategy Pattern**: Different movement algorithms
- **Template Method**: Common movement validation
- **Observer Pattern**: Logging and error reporting

### PatternGenerator (Core)
**Responsibility**: Generate coordinate sequences for various patterns
- **Categories**:
  - Geometric: Circle, square, triangle, star
  - Mathematical: Sine wave, spiral, figure-eight
  - Artistic: Heart, custom shapes
  - Random: Random walk, noise patterns

**Design Patterns**:
- **Factory Pattern**: Pattern creation methods
- **Builder Pattern**: Complex pattern construction
- **Command Pattern**: Pattern execution sequences

### GUI Interface
**Responsibility**: Graphical user interface using Tkinter
- **Components**:
  - Control panels for different pattern types
  - Real-time position display
  - Configuration sliders (speed, size)
  - Emergency stop button

**Design Patterns**:
- **MVC Pattern**: Model-View-Controller separation
- **Observer Pattern**: UI state updates
- **Command Pattern**: Button actions

### Console Interface
**Responsibility**: Text-based user interface
- **Features**:
  - Menu-driven navigation
  - Parameter input validation
  - Progress feedback
  - Error handling

**Design Patterns**:
- **State Pattern**: Menu navigation
- **Template Method**: Input processing
- **Strategy Pattern**: Different input types

## Data Flow

### Pattern Execution Flow
1. **User Input** → Interface captures user request
2. **Parameter Validation** → Validate coordinates, speeds, etc.
3. **Pattern Generation** → Create coordinate sequence
4. **Safety Check** → Validate all coordinates
5. **Movement Execution** → Execute via PyAutoGUI
6. **Feedback** → Log results and update UI

### Error Handling Flow
1. **Exception Detection** → Catch at multiple levels
2. **Error Classification** → Categorize error type
3. **Safety Response** → Emergency stop if needed
4. **User Notification** → Display appropriate message
5. **Recovery** → Return to safe state

## Configuration Management

### Settings Hierarchy
1. **Default Values** → Hard-coded safe defaults
2. **Configuration Files** → User preferences
3. **Runtime Parameters** → Session-specific settings
4. **Command Line Arguments** → Override options

### Safety Configuration
- **Failsafe Settings**: Always enabled by default
- **Speed Limits**: Prevent dangerous fast movements
- **Boundary Checking**: Screen edge validation
- **Emergency Stops**: Multiple stop mechanisms

## Threading Model

### GUI Threading
- **Main Thread**: GUI event handling
- **Worker Threads**: Movement execution
- **Synchronization**: Thread-safe state updates

### Safety Considerations
- **Thread Interruption**: Safe cancellation
- **Resource Cleanup**: Proper thread termination
- **State Consistency**: Atomic operations

## Extensibility Points

### Adding New Patterns
1. Add method to `PatternGenerator`
2. Register in interface menus
3. Add tests and documentation
4. Update help system

### Custom Movement Algorithms
1. Extend `MouseMover` class
2. Implement movement interface
3. Add safety validations
4. Update configuration

### Interface Extensions
1. Create new interface module
2. Implement common interface
3. Add to entry points
4. Update documentation

## Performance Considerations

### Optimization Strategies
- **Point Reduction**: Minimize unnecessary coordinates
- **Batch Processing**: Group similar operations
- **Caching**: Store calculated patterns
- **Lazy Loading**: Generate points on demand

### Memory Management
- **Pattern Cleanup**: Clear large coordinate arrays
- **Resource Limits**: Prevent memory exhaustion
- **Garbage Collection**: Proper object lifecycle

## Security & Safety

### Input Validation
- **Coordinate Bounds**: Screen boundary checking
- **Parameter Limits**: Reasonable value ranges
- **Type Checking**: Proper data types
- **Sanitization**: Clean user inputs

### Execution Safety
- **Emergency Stops**: Multiple stop mechanisms
- **Speed Limits**: Prevent dangerous movements
- **Permission Checks**: Verify system access
- **Error Recovery**: Graceful failure handling

## Testing Strategy

### Unit Testing
- **Core Logic**: MouseMover and PatternGenerator
- **Utility Functions**: Mathematical operations
- **Safety Mechanisms**: Boundary checking
- **Mock Testing**: Avoid actual mouse movement

### Integration Testing
- **Interface Integration**: GUI and console
- **Pattern Execution**: End-to-end testing
- **Error Scenarios**: Exception handling
- **Performance Testing**: Speed and memory

### Manual Testing
- **User Experience**: Interface usability
- **Safety Testing**: Emergency stops
- **Cross-Platform**: Different operating systems
- **Real-World Scenarios**: Practical usage
