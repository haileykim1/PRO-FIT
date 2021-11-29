package com.teamfour.myapplication

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.provider.MediaStore
import android.widget.Toast
import com.teamfour.myapplication.databinding.ActivityVirtualFittingBinding

class VirtualFittingActivity : BaseActivity() {

    val binding by lazy {ActivityVirtualFittingBinding.inflate(layoutInflater)}
    val REQUEST_VIDEO_CAPTURE = 1
    var videoUri:Uri? = null
    val REQUEST_VIDEO_GALLERY = 2

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        setTitle("MY VIDEO")

        init()
    }

    private fun init(){

        //새 영상 녹화
        binding.addVideoBtn.setOnClickListener {
            Toast.makeText(applicationContext,"영상에 전신이 나오도록 해주세요", Toast.LENGTH_LONG ).show()

            dispatchTakeVideoIntent()

        }

        //외부 스토리지에서 영상 선택
        binding.selectVideoBtn.setOnClickListener {
            var intent = Intent(Intent.ACTION_PICK)
            intent.data = MediaStore.Images.Media.EXTERNAL_CONTENT_URI
            intent.type = "video/*"
            startActivityForResult(intent, REQUEST_VIDEO_GALLERY)
        }
    }

    private fun dispatchTakeVideoIntent(){

        Intent(MediaStore.ACTION_VIDEO_CAPTURE).also{ videoIntent ->
            videoIntent.resolveActivity(packageManager)?.also{

                startActivityForResult(videoIntent, REQUEST_VIDEO_CAPTURE)
            }
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, intent: Intent?){
        super.onActivityResult(requestCode, resultCode, intent)

        if(resultCode == RESULT_OK){

            when(requestCode){
                REQUEST_VIDEO_GALLERY, REQUEST_VIDEO_CAPTURE ->{
                    videoUri= intent?.data!!
                    //videoView.setVideoURI(videoUri)
                    //binding.videoView.start()

                    //옷 고르기 액티비티로 넘어감
                    var intent: Intent = Intent(this, VirtualFittingClothesActivity::class.java)
                    intent.putExtra("videoUri", videoUri)
                    startActivity(intent)
                }
            }
        }

        //영상 출력 성공 확인
    }

}