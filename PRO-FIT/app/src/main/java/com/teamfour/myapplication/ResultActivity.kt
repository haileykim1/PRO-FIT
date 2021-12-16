package com.teamfour.myapplication

import android.content.ContentValues
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.ParcelFileDescriptor
import android.provider.MediaStore
import android.util.Log
import android.view.View.inflate
import android.widget.Toast
import com.teamfour.myapplication.databinding.ActionBarLayoutBinding.inflate
import com.teamfour.myapplication.databinding.ActivityResultBinding
import com.teamfour.myapplication.databinding.ActivityVirtualFittingClothesBinding
import java.io.File
import java.io.FileOutputStream
import java.net.URL
import java.text.SimpleDateFormat
import java.util.*

class ResultActivity : BaseActivity() {

    val binding by lazy { ActivityResultBinding.inflate(layoutInflater)}

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)
        init()
    }
    private fun init(){
        binding.videoView.setVideoPath("android.resource://" + packageName + "/raw/realoutput1")

        binding.playBtn.setOnClickListener {
            binding.videoView.start()
        }
        binding.downloadBtn.setOnClickListener {
            saveFileToGallery()

        }
    }
    fun saveFileToGallery(){

        //media item
        val resolver = applicationContext.contentResolver

        val item = ContentValues().apply{
            put(MediaStore.Video.Media.DISPLAY_NAME, "profit" + SimpleDateFormat("HH:mm:ss").format(System.currentTimeMillis()) + ".mp4")
            put(MediaStore.Video.Media.MIME_TYPE, "video/mp4")
            put(MediaStore.Video.Media.IS_PENDING, 1)
        }

        val uri = resolver.insert(MediaStore.Video.Media.EXTERNAL_CONTENT_URI, item)?.let{uri ->
            resolver.openFileDescriptor(uri, "w", null).use{ parcelFileDescriptor ->
                parcelFileDescriptor?.run{
                    //outputstream에 write
                    FileOutputStream(this.fileDescriptor).use{outputStream ->
                        val videoInputStream = resources.openRawResource(R.raw.realoutput1)
                        while(true){
                            val data = videoInputStream.read()
                            if(data == -1){
                                break
                            }
                            outputStream.write(data)
                        }
                        videoInputStream.close()
                        outputStream.close()
                    }
                }
            }
            if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q){
                item.clear()
                item.put(MediaStore.Video.Media.IS_PENDING, 0)
                resolver.update(uri, item, null, null)
            }
        }


        

        Toast.makeText(applicationContext, "download completed", Toast.LENGTH_SHORT).show()
    }
}