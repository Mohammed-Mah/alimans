< !DOCTYPE html >

    <
    html lang = "en" >

    <
    head >

    <
    meta charset = "UTF-8" >

    <
    meta name = "viewport"
content = "width=device-width, initial-scale=1.0" >

    <
    title > 3 D Visualization with Three.js < /title>

<
script src = https: //cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js></script>

    <
    style >

    body {

        margin: 0;

        overflow: hidden;

    }

<
/style>

<
/head>

<
body >

    <
    script >

    // Create the scene

    const scene = new THREE.Scene();



// Create a camera, which determines what we'll see when we render the scene

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

camera.position.z = 5;



// Create a WebGL renderer and attach it to our document

const renderer = new THREE.WebGLRenderer();

renderer.setSize(window.innerWidth, window.innerHeight);

document.body.appendChild(renderer.domElement);



// Create a cube

const geometry = new THREE.BoxGeometry();

const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });

const cube = new THREE.Mesh(geometry, material);



// Add the cube to the scene

scene.add(cube);



// Animation loop

function animate() {

    requestAnimationFrame(animate);



    // Rotate the cube for some movement

    cube.rotation.x += 0.01;

    cube.rotation.y += 0.01;



    // Render the scene from the perspective of the camera

    renderer.render(scene, camera);

}

animate();



// Handle window resize

window.addEventListener('resize', () => {

    renderer.setSize(window.innerWidth, window.innerHeight);

    camera.aspect = window.innerWidth / window.innerHeight;

    camera.updateProjectionMatrix();

});

<
/script>

<
/body>

<
/html>