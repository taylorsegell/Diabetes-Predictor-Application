"""Plotly Dash HTML layout override."""

html_layout = """
<!doctype html>
<html lang="en" class="h-100">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <!-- Google Fonts -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"/>
    <!-- Custom CSS for Dash -->
    <link rel="stylesheet" href="/static/dashstyles.css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="/static/style.css">

    <!-- bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" async integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
    <title>Visual Overview</title>
</head>
<body class="d-flex flex-column h-100 body">
<nav class="navbar navbar-expand-lg navbar-dark shadow">
    <div class="container">
        <a class="navbar-brand" href="#" style="display: flex;">
            <div style="width:30px;margin-right: 1rem;">
            <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"
                id="Layer_1" x="0px" y="0px" viewBox="0 0 32 32" style="enable-background:new 0 0 32 32;" style="width:30%;"
                xml:space="preserve">
                <path id="medical_1_" fill="white"
                    d="M16,31.36c-0.199,0-0.36-0.161-0.36-0.36v-8c0-0.199,0.161-0.36,0.36-0.36s0.36,0.161,0.36,0.36v8  C16.36,31.199,16.199,31.36,16,31.36z M14.382,27.186c-0.047,0-0.095-0.01-0.141-0.029c-0.999-0.427-1.697-1.533-1.697-2.692  c0-1.22,0.518-2.151,1.631-2.932c0.164-0.113,0.387-0.074,0.501,0.088c0.114,0.163,0.075,0.388-0.088,0.502  c-0.928,0.65-1.325,1.352-1.325,2.342c0,0.879,0.518,1.714,1.259,2.03c0.183,0.078,0.268,0.289,0.19,0.473  C14.655,27.104,14.522,27.186,14.382,27.186z M17.617,27.186c-0.108,0-0.216-0.05-0.287-0.143c-0.12-0.158-0.089-0.385,0.069-0.505  c0.924-0.7,1.335-1.204,1.335-2.335c0-1.4-1.379-2.346-2.839-3.346c-1.642-1.125-3.339-2.288-3.339-4.272  c0-1.106,0.649-2.115,1.654-2.57c0.181-0.08,0.395-0.001,0.477,0.18s0.001,0.395-0.18,0.477c-0.748,0.338-1.231,1.089-1.231,1.914  c0,1.604,1.47,2.612,3.026,3.679c1.55,1.062,3.153,2.159,3.153,3.939c0,1.412-0.569,2.111-1.62,2.909  C17.77,27.161,17.693,27.186,17.617,27.186z M17.617,19.845c-0.108,0-0.216-0.05-0.287-0.143c-0.12-0.159-0.089-0.385,0.069-0.505  c0.924-0.699,1.335-1.202,1.335-2.334c0-1.25-1.1-2.138-2.375-3.025v4.164c0,0.199-0.161,0.36-0.36,0.36s-0.36-0.161-0.36-0.36  v-4.659c-1.558-1.072-3.084-2.215-3.084-4.097c0-1.107,0.649-2.116,1.654-2.57c0.181-0.08,0.395-0.001,0.477,0.18  s0.001,0.395-0.18,0.477c-0.748,0.338-1.231,1.089-1.231,1.914c0,1.374,1.078,2.31,2.364,3.22V5.333c-1.131-0.174-2-1.154-2-2.333  c0-1.301,1.059-2.36,2.36-2.36c1.302,0,2.36,1.059,2.36,2.36c0,1.179-0.869,2.159-2,2.333v7.63c1.532,1.049,3.095,2.142,3.095,3.9  c0,1.413-0.569,2.113-1.62,2.909C17.77,19.82,17.693,19.845,17.617,19.845z M16,4.639c0.01,0,0.02,0,0.03,0.001  c0.89-0.016,1.61-0.745,1.61-1.64c0-0.904-0.735-1.64-1.64-1.64S14.36,2.096,14.36,3c0,0.895,0.72,1.624,1.61,1.64  C15.98,4.639,15.99,4.639,16,4.639z M19,13.36c-0.135,0-0.265-0.076-0.325-0.207c-0.085-0.18-0.008-0.394,0.172-0.479  c1.041-0.491,1.888-1.88,1.888-3.098c0-1.894,1.059-2.936,2.979-2.936H30c0.199,0,0.36,0.161,0.36,0.36S30.199,7.36,30,7.36h-6.286  c-1.178,0-1.875,0.411-2.138,1.28H28c0.199,0,0.36,0.161,0.36,0.36S28.199,9.36,28,9.36h-6.54c-0.004,0.07-0.005,0.142-0.005,0.216  c0,0.334-0.057,0.698-0.164,1.065h4.688c0.199,0,0.36,0.161,0.36,0.36s-0.161,0.36-0.36,0.36h-4.963  c-0.392,0.819-1.03,1.572-1.862,1.964C19.104,13.349,19.052,13.36,19,13.36z M13,13.36c-0.052,0-0.104-0.011-0.153-0.034  c-0.832-0.392-1.47-1.145-1.861-1.964H6c-0.199,0-0.36-0.161-0.36-0.36s0.161-0.36,0.36-0.36h4.71  c-0.107-0.368-0.163-0.731-0.163-1.065c0-0.074-0.002-0.146-0.005-0.216H4C3.801,9.36,3.64,9.199,3.64,9S3.801,8.64,4,8.64h6.426  c-0.263-0.869-0.96-1.28-2.138-1.28H2C1.801,7.36,1.64,7.199,1.64,7S1.801,6.64,2,6.64h6.288c1.684,0,2.704,0.801,2.931,2.273  c0.005,0.023,0.009,0.046,0.01,0.071c0.025,0.187,0.038,0.384,0.038,0.592c0,1.218,0.846,2.608,1.886,3.098  c0.18,0.085,0.257,0.299,0.172,0.479C13.264,13.284,13.135,13.36,13,13.36z M17.617,12.361c-0.113,0-0.225-0.053-0.295-0.153  c-0.114-0.163-0.074-0.387,0.088-0.501c0.929-0.651,1.324-1.352,1.324-2.342c0-0.879-0.518-1.713-1.259-2.03  c-0.183-0.078-0.268-0.29-0.189-0.472c0.078-0.183,0.291-0.268,0.473-0.19c0.998,0.426,1.696,1.533,1.696,2.692  c0,1.22-0.519,2.151-1.631,2.932C17.761,12.34,17.688,12.361,17.617,12.361z">
                </path>    
            </svg> </div>IBM Diabetes Prevention
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a class="nav-link " href="/">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link " href="/diagnose">Predictor</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link active" href="#">Visual Overview</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link " href="/about">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link " href="/report">Report</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
<main role="main" class="flex-shrink-0">
    <div class="container shadow rounded fadeIn p-5 my-5 bg-white" id="content">

    <h2> Data Visualization </h2>
    <br>
            {%app_entry%}
    </div>
</main>
<footer class="footer mt-auto py-3 text-white">
    <div class="container">
        <div class="d-flex justify-content-between">
            <div>
                <span class="text-white small">Taylor Segell May 2023</span>
            </div>
            <div class>
                <a class="text-white text-decoration-none" href="https://github.com/">View the source on Github <i class="fa fa-github"></i></a>
            </div>
        </div>
    </div>
                {%config%}
                {%scripts%}
                {%renderer%}
</footer>
</body>
</html>
"""
