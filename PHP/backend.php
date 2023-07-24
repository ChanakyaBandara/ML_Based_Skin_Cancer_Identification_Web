 <?php
  date_default_timezone_set("asia/colombo");
  require 'file_upload.php';
  define('orginal_dir', 'uploads');

  if (isset($_FILES['File'])) {

    $file_new_name = "0";
    $file_orginal_name = "0";

    if ($_FILES['File']['size'] <> 0) {
      $file = $_FILES['File'];
      $allowd = array('png', 'jpg', 'jpeg');
      $fileDestination = orginal_dir;
      $file_orginal_name = $file['name'];
      $file_new_name = uploadfile($file, $allowd, $fileDestination);
      $shelloutput = detection($file_new_name);
      $resultObj = json_decode(file_get_contents("result.json"));
      $myObj=new stdClass;
      $myObj->shelloutput = $shelloutput;
      $myObj->result = $resultObj[0];
      echo json_encode($myObj);
    }
  }

  function detection($var1)
  {
    $command1 =  'python main.py ' . $var1;
    $command = escapeshellcmd($command1);
    $output = shell_exec($command);
    return $output;
  }
  ?>
