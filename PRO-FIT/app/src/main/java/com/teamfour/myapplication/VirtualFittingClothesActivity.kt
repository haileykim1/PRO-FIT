package com.teamfour.myapplication

import android.content.Intent
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.teamfour.myapplication.databinding.ActivityVirtualFittingBinding
import com.teamfour.myapplication.databinding.ActivityVirtualFittingClothesBinding

class VirtualFittingClothesActivity : BaseActivity() {

    val binding by lazy { ActivityVirtualFittingClothesBinding.inflate(layoutInflater)}

    var videoUri: Uri? = null
    var clothesNum: Int? = null


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        init()
    }
    private fun init(){

        val videoIntent = getIntent()
        videoUri = videoIntent.getParcelableExtra("videoUri")

        //가상피팅영상선택화면으로 백
        binding.backToVirtualBtn.setOnClickListener {
            finish()
        }

        binding.clothes0.setOnClickListener {
            clothesNum = 0
            startProcessing()
        }
        binding.clothes1.setOnClickListener {
            clothesNum = 1
            startProcessing()
        }
        binding.clothes2.setOnClickListener {
            clothesNum = 2
            startProcessing()
        }


    }

    private fun startProcessing(){
        Toast.makeText(this, "가상피팅 처리", Toast.LENGTH_LONG).show()
    }

}