<template>
  <div id="mpbox">
    <div class="back2"></div>
    <br>
    <h1 id="mptitle">My Page</h1>
    <hr id="hr">
    <div>
    <img id="img1" src="https://mblogthumb-phinf.pstatic.net/20160630_260/thatkxkd1022_1467297390929WBX1v_JPEG/Zootopia_%282%29.jpg?type=w2" alt="">
    </div>
    <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="username">
    <br><br><br><br><br><br><br><br>
    <button type="button" class="btn btn-light" id="btn1" onclick="changeImg()"><p id="editid">edit</p></button>
    <br><br><br><br><br><br><br><br><br><br><br>
    <hr id="hr">
    <h1 id="mbtititle">ISTJ</h1>
    <img id="mbtiimg" src="https://p4.wallpaperbetter.com/wallpaper/1021/34/573/zoe-saldana-as-gamora-wallpaper-preview.jpg" alt="">
    <img id="mbtiimg" src="https://mblogthumb-phinf.pstatic.net/MjAxNjEyMjhfNjEg/MDAxNDgyOTE4NTU1ODk3.VEv5GJnfLuoMBAmCjxdjzsnfaGcTBeaKeaJxKTchwJog.4sXM4OJXABudSakvk1kz3V3hiZbYOBnOKtx9kkGUVFkg.JPEG.jshn0107/111.jpg?type=w800" alt="">
    <br><br><br><br><br><br><br><br><br><hr>
    <h1 id="mbtititle">ESTJ</h1>
    <img id="mbtiimg" src="https://blog.kakaocdn.net/dn/DhCxg/btqCKAY303E/ZuyIeKiYWOBCn1d7UJHs11/img.jpg" alt="">
  </div>
</template>

<script>
export default {
  name: 'MyPageView',
}
</script>

<script>
function changeImg(){
  var img1 = document.getElementById("img1")
  img1.src="https://p4.wallpaperbetter.com/wallpaper/1021/34/573/zoe-saldana-as-gamora-wallpaper-preview.jpg"
}
</script>




<style scoped>
/* #mpbox{
  margin: auto;
  width: 90%;
  height: 800px;
  border-radius:10% ;
  border: 1px solid lightgray;
} */

div.back2 {
  width: 100vw;
  height: 190vh;
  position: absolute;
  background-color: black;
  z-index: -1;
}

#mptitle{
  color: rgba(211, 211, 211, 0.99);
  font-weight: bold;
  font-size: 40px;
  padding-top: 40px;
  text-align: left;
  padding-left: 20px;
}

#hr{
  width: 1600px;
  margin-left: 20px;
  
}
#img1{
  width: 200px;
  height: 185px;
  float: left;
  margin-left: 20px;
  border-radius: 6%;
}

img{
  width: 200px;
  float: left;
  margin-left: 20px;
  border-radius: 6%;
}

#exampleFormControlInput1{
  float: left;
  margin-left: 25px;
  
}

#btn1{
  width: 200px;
  font-size: 20px;
  font-weight: bold;
  float: left;
  margin-left: 20px;
  
}

#editid{
  color: rgb(78, 78, 78);
}

#mbtititle{
  color: rgba(211, 211, 211, 0.99);
  font-weight: bold;
  font-size: 40px;
  text-align: left;
  padding-left: 20px;
}

#mbtiimg{
  width: 200px;
  height: 180px;
}

</style>