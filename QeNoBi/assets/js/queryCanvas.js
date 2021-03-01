var empty = false
var path = new Path();


path.segments = [];
path.add({x: 20, y: 100});
path.add({x: 100, y: 20});
path.add({x: 190, y: 90});
path.smooth();

//path.selected;

path.strokeColor = 'black';
path.strokeWidth = 5;

// Fully select the path, so we can see its handles:
path.fullySelected = true;

var hitOptions = {
    segments: true,
    handles: true,
    stroke: true,
    fill: true,
    tolerance: 5
};

var segment, path, handle;
var movePath = false;

function onMouseDown(event) {
    segment = path = handle = null;
    var hitResult = project.hitTest(event.point, hitOptions);

    if (event.modifiers.shift) {
        if (hitResult.type == 'segment') {
            hitResult.segment.remove();
        }
        ;
        return;
    }

    if (hitResult) {
        path = hitResult.item;
        if (hitResult.type == 'segment') {
            segment = hitResult.segment;
        } else if (hitResult.type == 'stroke') {
            var location = hitResult.location;
            segment = path.insert(location.index + 1, event.point);
            path.smooth();
        } else if (hitResult.type == 'handle-in') {
            handle = hitResult.segment.handleIn;
        } else if (hitResult.type == 'handle-out') {
            handle = hitResult.segment.handleOut;
        }
    }
    movePath = hitResult.type == 'fill';
    if (movePath)
        project.activeLayer.addChild(hitResult.item);

    path.fullySelected = true;
}


function onMouseDrag(event) {
    if (segment) {
        segment.point = event.point;
        path.smooth();
    }

    if (handle) {
        handle.x += event.delta.x;
        handle.y += event.delta.y;
    }


    if (movePath)
        path.position += event.delta;
}

$("#query-clear-button").click(function () {
    project.clear()
    empty = true
})
console.log("Last element ", path.segments)