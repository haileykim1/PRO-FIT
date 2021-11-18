package com.teamfour.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.teamfour.myapplication.databinding.ActivityProfileBinding

class ProfileActivity : BaseActivity() {

    val binding by lazy {ActivityProfileBinding.inflate(layoutInflater)}

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        setTitle("MY PROFILE")
    }
}